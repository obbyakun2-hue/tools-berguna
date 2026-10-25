# Instagram — Graph API RESMI Meta

Untuk akun **Bisnis/Kreator milik sendiri**: statistik, daftar media, posting via API, dan (dengan App Review) balas DM/komen.

1. Jadikan akun IG kamu Bisnis/Kreator & hubungkan ke Facebook Page
2. Di https://developers.facebook.com buat App → tambahkan **Instagram Graph API** → generate token + ambil IG User ID
3. `pip install -r requirements.txt`, copy `.env.example` jadi `.env`, isi token & ID
4. `python contoh.py`

**Batas jujurnya:** API resmi tidak bisa melihat follower akun privat orang lain, tidak bisa auto-follow/like massal, dan DM/komen untuk publik butuh App Review Meta. Tool yang menjanjikan itu semua = scraping tidak resmi, risiko akun kena ban.
