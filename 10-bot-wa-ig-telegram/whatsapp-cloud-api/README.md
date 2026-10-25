# Bot WhatsApp — Cloud API RESMI Meta

Jalur resmi = nomor aman, bisa untuk bisnis. Gratis nomor tes dari Meta untuk belajar.

1. Buka https://developers.facebook.com → buat App → tambahkan produk **WhatsApp**
2. Ambil `WA_TOKEN` + `PHONE_NUMBER_ID` dari panel WhatsApp > API Setup
3. `npm install`, copy `.env.example` jadi `.env`, isi semua nilainya
4. `node bot.js` — lalu buat URL publik HTTPS (Cloudflare Tunnel / ngrok) dan daftarkan `https://url-kamu/webhook` di dashboard Meta, isi Verify Token yang sama dengan `.env`
5. Chat nomor tes dari HP kamu → bot membalas

**Aturan penting Meta:** membalas bebas hanya dalam 24 jam sejak user chat terakhir. Di luar itu / untuk menyapa duluan: wajib *template message* yang disetujui + user harus opt-in. Melanggar = nomor dibatasi.
