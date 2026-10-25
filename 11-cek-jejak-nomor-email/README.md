# 🔎 11 — Cek Jejak Nomor HP & Email (Audit Punya Sendiri)

## ⚠️ Batas Jujurnya Dulu — Baca Ini

**Tidak ada tool — gratis maupun berbayar — yang bisa menampilkan daftar lengkap "nomor HP ini terdaftar di aplikasi apa saja + email apa saja".**

Alasannya sederhana: daftar itu data internal tiap perusahaan (WhatsApp, Gojek, bank, dll) dan tidak pernah dibuka ke publik / pihak ketiga. Yang benar-benar bisa dicek hanyalah:

1. Apakah nomor/email kamu pernah **bocor** dalam insiden data breach yang diketahui publik
2. Di akun **milikmu sendiri**, saat kamu login — aplikasi apa yang masih menautkan nomor/email itu, perangkat & sesi apa yang masih aktif
3. Bagaimana nomor kamu **diberi nama/tag oleh orang lain** di aplikasi identifikasi nomor (crowdsource)
4. Untuk nomor **tak dikenal / diduga penipu**: apakah nomor itu sudah dilaporkan sebagai spam/penipuan

> Situs / aplikasi / bot Telegram yang mengklaim bisa membuka "semua akun + semua email dari 1 nomor HP" hampir pasti **scam**: ujungnya minta bayar, minta OTP, atau mencuri data yang kamu masukkan. Jangan pernah masukkan OTP, password, PIN, atau NIK ke tool semacam itu.

Folder ini isinya tool & panduan **resmi untuk mengaudit nomor & email kamu SENDIRI** (atau nomor mencurigakan yang menghubungimu, sebatas cek spam/penipuan).

---

## A. Cek Kebocoran (Breach) — Nomor & Email Kamu

| Tool | Link Resmi | Yang Dicek | Catatan |
|---|---|---|---|
| **Have I Been Pwned** | https://haveibeenpwned.com | Email + nomor HP (format internasional, contoh `62812xxxxxxx`) | Standar emas. Menampilkan layanan apa yang bocor + jenis data apa saja. Aktifkan juga menu **Notify me** biar dapat email kalau ada bocoran baru. |
| **PeriksaData** | https://periksadata.com | Email & nomor telepon, fokus kebocoran Indonesia | Cocok untuk cek insiden lokal |
| **Mozilla Monitor** | https://monitor.mozilla.org | Email + panduan langkah menghapus data dari broker | Gratis, perlu akun Mozilla untuk pemantauan berkala |
| **XposedOrNot** | https://xposedornot.com | Email | Alternatif open-source untuk pembanding |
| **F-Secure Identity Theft Checker** | https://www.f-secure.com/en/identity-theft-checker | Email | Cek cepat tanpa daftar |

**Kalau hasilnya kena bocor:** ganti password layanan itu + semua layanan yang password-nya sama, nyalakan 2FA mulai dari email utama dulu.

## B. Cek Email Ini Terdaftar di Situs Apa Saja — Untuk Email Sendiri

| Tool | Link | Cara Kerja |
|---|---|---|
| **holehe** | https://github.com/megadose/holehe | Tool open-source (Python) yang mengecek apakah **email kamu sendiri** terdaftar di 100+ situs populer. Jalan lokal: `pip install holehe` lalu `holehe email@kamu.com`. Hasilnya perkiraan (berbasis respon situs), bukan bukti mutlak — verifikasi dengan login langsung. |
| **Kotak masuk email kamu sendiri** | — | Cara paling akurat justru manual: cari di Gmail dengan kata `welcome`, `verify`, `konfirmasi`, `pendaftaran`, `your account` — semua layanan yang pernah kamu daftari mengirim email sambutan/verifikasi. |
| **Password manager (Bitwarden)** | https://bitwarden.com | Semua login yang pernah kamu simpan = daftar akunmu yang sebenarnya. Audit dari sini, hapus yang sudah tidak dipakai. |

> holehe & tool sejenis hanya untuk email/nomor **milikmu sendiri atau yang sudah memberimu izin tertulis**. Memakainya untuk memetakan akun orang lain = mengintai, dan hasilnya pun sering salah.

## C. Cek Info Dasar & Reputasi Nomor HP

| Tool | Link | Yang Bisa Dilihat |
|---|---|---|
| **PhoneInfoga** | https://github.com/sundowndev/phoneinfoga | Info dasar nomor secara lokal: format internasional, negara, operator (perkiraan). **Tidak** membuka nama/akun pemilik. |
| **Script lokal repo ini** | `cek-format-nomor.py` di folder ini | Versi ringkas tanpa install server: ubah `08xx` → `+62xx`, tampilkan format untuk HIBP & info format dasar. 100% offline. |
| **Getcontact** | https://www.getcontact.com | Tag/nama penyimpanan nomor oleh pengguna lain + label spam. Berguna 2 arah: cek nomormu sendiri disimpan sebagai apa, dan cek nomor tak dikenal yang menghubungimu. ⚠️ Aplikasi ini meminta akses kontakmu — pertimbangkan privasinya. |
| **Truecaller** | https://www.truecaller.com | Identifikasi penelepon + skor spam global. Peringatan privasi sama seperti Getcontact. |
| **CekRekening.id (Kominfo)** | https://cekrekening.id | Cek apakah **nomor rekening / nomor HP** pernah dilaporkan terkait penipuan di Indonesia. Untuk nomor mencurigakan, bukan untuk mengintip orang. |

## D. Tempat Sebenarnya Melihat "Nomor/Email Ini Tertaut di Mana"

Tidak ada jalan pintas — yang resmi adalah dari dalam akunmu sendiri:

| Layanan | Menu yang Dicek |
|---|---|
| Google | myaccount.google.com → Keamanan → Perangkat Anda, Aktivitas masuk, Akses pihak ketiga |
| WhatsApp | Profil (nomor terdaftar) → Perangkat Tertaut → keluarkan sesi asing |
| Telegram | Settings → Devices + Privacy and Security → keluarkan sesi asing, cek nomor yang tampil |
| Instagram / Facebook | Accounts Center → Info pribadi (email & nomor tertaut) → Kata sandi & keamanan → Tempat Anda login |
| Apple ID | appleid.apple.com → Perangkat + email/nomor yang bisa dihubungi |
| TikTok / X / e-wallet / bank | Pengaturan → Akun/Keamanan → nomor & email terdaftar + perangkat yang masuk |

Panduan langkah demi langkah + daftar centang ada di [`CHECKLIST-AUDIT.md`](CHECKLIST-AUDIT.md).

## Yang SENGAJA Tidak Ada di Folder Ini
- Script memetakan akun orang lain dari nomor HP-nya (stalking/doxxing)
- Cara menyalahgunakan fitur "lupa password" untuk mengintip potongan email / foto profil akun orang lain
- Database bocor mentah (DeHashed berbayar, Snusbase, dll) untuk mencari data orang — itu perdagangan data curian
- Tool "lacak lokasi HP dari nomor" — secara teknis tidak ada yang sah untuk publik; yang beredar = scam / malware

Kalau tujuanmu **nomor penipu**: kumpulkan bukti chat + transfer, cek nomornya di Getcontact/CekRekening, lalu laporkan ke bank, platform, dan polisi. Itu jalur yang benar-benar menghasilkan tindakan.
