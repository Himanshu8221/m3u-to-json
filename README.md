<h1 align="center">📺 M3U Playlist Merger & Metadata Extractor</h1>

<p align="center">
  A powerful and flexible IPTV playlist parser for .m3u / .m3u8 streams.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.7%2B-blue?logo=python" />
  <img src="https://img.shields.io/badge/license-MIT-green" />
  <img src="https://img.shields.io/badge/iptv-extended%20metadata-orange" />
</p>

---

### 🌟 Features

- 🔗 **Multiple M3U URL Support** – Merge as many playlists as you want
- 🧠 **Smart Metadata Extraction** – Grabs:
  - `tvg-id`, `tvg-name`, `group-title`, `tvg-logo`
  - `display-name`, `license_key`, `license_type`
  - `user_agent`, `cookie`, `url`, and more
- ⚙️ Parses extended M3U tags:
  - `#EXTINF`, `#EXTVLCOPT`, `#KODIPROP`, `#EXTHTTP`
- 💾 Outputs a well-formatted `playlist.json` with all channel info
- 📡 Supports `.m3u8`, `.mpd`, and other IPTV stream types

---

### 📂 Output Example

```json
{
  "tvg-id": "441408",
  "tvg-name": "Aaj Tak",
  "group-title": "News",
  "tvg-logo": "https://jiotvimages.cdn.jio.com/dare_images/images/Aaj_Tak.png",
  "display-name": "Aaj Tak",
  "user_agent": "Mozilla/5.0 (Windows NT 10.0...)",
  "license_key": "5181d3e6...:3dca7917...",
  "cookie": "__hdnea__=st=17525...",
  "url": "https://z5ak-cmaflive.zee5.com/.../index.m3u8"
}
