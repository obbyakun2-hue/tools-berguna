"""
Instagram Graph API (RESMI Meta) — contoh baca akun BISNIS/KREATOR milik sendiri.
Install : pip install -r requirements.txt
Isi .env: IG_ACCESS_TOKEN + IG_USER_ID dari developers.facebook.com
          (App -> Instagram Graph API; akun IG harus terhubung ke Facebook Page)
Jalankan: python contoh.py
Yang dilakukan: tampilkan profil, daftar media terakhir, dan insight sederhana.
Ini jalur resmi untuk: posting terjadwal, balas DM/komen (perlu permission + App Review),
dan statistik akun. BUKAN scraping — tidak membaca akun orang lain tanpa izin mereka.
"""
import os, requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ["IG_ACCESS_TOKEN"]
IG_ID = os.environ["IG_USER_ID"]
API = "https://graph.facebook.com/v21.0"

def get(path, **params):
    r = requests.get(f"{API}/{path}", params={"access_token": TOKEN, **params}, timeout=30)
    r.raise_for_status()
    return r.json()

print("== Profil ==")
print(get(IG_ID, fields="username,followers_count,media_count,account_type"))

print("\n== 5 Media Terakhir ==")
media = get(f"{IG_ID}/media", fields="id,caption,media_type,permalink,timestamp,like_count,comments_count", limit=5)
for m in media.get("data", []):
    print("-", m.get("timestamp"), m.get("media_type"), "❤", m.get("like_count", 0), "|", (m.get("caption") or "")[:60])

# Contoh insight (butuh permission instagram_manage_insights):
# print(get(f"{IG_ID}/insights", metric="impressions,reach,profile_views", period="day"))
