# 🤖 10 — Tools & Script Bot WA • IG • Telegram

Bot yang **resmi & aman** per platform. Baca kolom "Jalur" baik-baik — jalur tidak resmi berisiko akun diblokir.

## Ringkasan Cepat

| Platform | Jalur Resmi (disarankan) | Framework / Tool | Folder Script di Repo Ini |
|---|---|---|---|
| **Telegram** | ✅ Bot API via @BotFather — bebas, tanpa approval | python-telegram-bot, aiogram, Telegraf, grammY | `telegram/` |
| **WhatsApp** | ✅ WhatsApp Cloud API (Meta) — perlu akun Meta Business, template message untuk broadcast | Node/Python + webhook, ManyChat, Chatfuel (no-code) | `whatsapp-cloud-api/` |
| **Instagram** | ✅ Instagram Graph API (Meta) — untuk akun Bisnis/Kreator, perlu App Review untuk publik | Graph API + webhook DM/komen, ManyChat, Chatfuel | `instagram-graph-api/` |
| **Multi-channel** | ✅ Satu dashboard untuk WA+IG+Messenger | ManyChat, Chatfuel, n8n (otomasi) | — |

## ⚠️ Soal Library Tidak Resmi — Jujur, Tanpa Ditutupi
Library seperti **Baileys / whatsapp-web.js** (WhatsApp) dan **instagrapi / Instaloader scraping** (Instagram) itu **TIDAK resmi**: mereka meniru aplikasi web / meminjam sesi login.
- Risikonya nyata: nomor/akun bisa **diblokir permanen**, sesi sering putus saat platform update, dan scraping massal melanggar Ketentuan Layanan Meta.
- Di repo ini library itu **hanya disebut sebagai pengetahuan**, tidak disediakan script-nya, dan tidak disarankan untuk akun utama / nomor penting.
- Kalau tetap penasaran, pakai HANYA akun & nomor cadangan untuk belajar — risikonya tanggung sendiri.
- Untuk jualan / bisnis / akun utama: selalu jalur resmi di tabel atas.

## Tools Pendukung Bot (semua platform)
| Tool | Link | Fungsi |
|---|---|---|
| **BotFather** | https://t.me/BotFather | Buat bot & ambil token Telegram (resmi, di dalam Telegram) |
| **Meta for Developers** | https://developers.facebook.com | Daftar app untuk WA Cloud API & IG Graph API |
| **n8n** | https://n8n.io | Otomasi visual: hubungkan bot ↔ Google Sheets / AI / database (bisa self-host gratis) |
| **Cloudflare Tunnel** | https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/ | Webhook lokal jadi HTTPS publik tanpa buka port (pengganti ngrok) |
| **Docker** | https://www.docker.com | Deploy bot 24 jam di VPS/PC |
| **Postman / Bruno** | https://www.usebruno.com | Tes webhook & API sebelum coding |

## Isi Folder Script
- [`telegram/python-telegram-bot/`](telegram/python-telegram-bot/) — bot Python: /start, /help, /id, echo. Token dari env, siap jalan.
- [`telegram/telegraf-node/`](telegram/telegraf-node/) — versi Node.js yang sama ringannya.
- [`whatsapp-cloud-api/`](whatsapp-cloud-api/) — server webhook Node.js RESMI Meta: verifikasi webhook + balas pesan masuk.
- [`instagram-graph-api/`](instagram-graph-api/) — contoh Python RESMI: ambil profil, media & insight akun bisnis sendiri.

Semua script: **token TIDAK ditulis di kode** — pakai file `.env` (lihat `.env.example` di tiap folder), dan `.env` sudah masuk `.gitignore`.
