import requests
import json
import re

# 🔁 List of M3U URLs to parse and merge
m3u_urls = [
    "https://himanshu-iptv.short.gy/iptv" # Add more links as needed
]

def parse_extinf_line(line):
    # Extract all key="value" pairs
    props = dict(re.findall(r'(\S+?)="(.*?)"', line))
    # Extract display-name (text after the last comma)
    display_name_match = re.search(r',([^,]+)$', line)
    if display_name_match:
        props["display-name"] = display_name_match.group(1).strip()
    return props

def fetch_and_parse_m3u(m3u_url):
    print(f"📥 Fetching: {m3u_url}")
    try:
        response = requests.get(m3u_url)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Failed to fetch {m3u_url}: {e}")
        return []

    lines = response.text.splitlines()
    channels = []
    current = {}

    for line in lines:
        line = line.strip()

        if line.startswith("#EXTINF"):
            current = parse_extinf_line(line)

        elif line.startswith("#KODIPROP:"):
            key_val = line[len("#KODIPROP:"):].split("=", 1)
            if len(key_val) == 2:
                key, val = key_val
                current[key.strip()] = val.strip()

        elif line.startswith("#EXTVLCOPT:"):
            key_val = line[len("#EXTVLCOPT:"):].split("=", 1)
            if len(key_val) == 2:
                key, val = key_val
                if key.strip().lower() == "http-user-agent":
                    current["user_agent"] = val.strip()
                else:
                    current[key.strip()] = val.strip()

        elif line.startswith("#EXTHTTP:"):
            try:
                http_data = json.loads(line[len("#EXTHTTP:"):])
                current.update(http_data)
            except Exception as e:
                current["http_data_parse_error"] = str(e)

        elif line.startswith("http"):
            current["url"] = line
            channels.append(current)
            current = {}

    print(f"✅ Found {len(channels)} channels in {m3u_url}")
    return channels

if __name__ == "__main__":
    all_channels = []
    for url in m3u_urls:
        channels = fetch_and_parse_m3u(url)
        all_channels.extend(channels)

    output_file = "playlist.json"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(all_channels, f, indent=2, ensure_ascii=False)
        print(f"🎉 All merged: {len(all_channels)} total channels saved to {output_file}")
    except Exception as e:
        print(f"❌ Failed to write file: {e}")
