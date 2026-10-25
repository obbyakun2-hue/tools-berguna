"""
Cek format nomor HP secara LOKAL (offline, tanpa kirim data ke mana pun).
Fungsi: normalisasi nomor Indonesia 08xx -> +62xx / 62xx untuk dipakai
di Have I Been Pwned, dan menampilkan info format dasar.

Jalankan: python cek-format-nomor.py 0812xxxxxxx
Opsional (info operator/tipe lebih akurat): pip install phonenumbers
Tool ini TIDAK mencari pemilik, akun, atau lokasi nomor — itu tidak bisa
dilakukan secara sah dari nomor saja.
"""
import re, sys

def normalisasi(raw: str) -> str:
    n = re.sub(r"[^\d+]", "", raw)
    if n.startswith("+62"): return n
    if n.startswith("62"): return "+" + n
    if n.startswith("0"): return "+62" + n[1:]
    if n.startswith("8"): return "+62" + n
    return n

def main():
    if len(sys.argv) < 2:
        print("Pakai: python cek-format-nomor.py 0812xxxxxxx"); return
    intl = normalisasi(sys.argv[1])
    print(f"Format internasional : {intl}")
    print(f"Format untuk HIBP    : {intl.lstrip('+')}   -> tempel di https://haveibeenpwned.com")
    print(f"Panjang digit        : {len(re.sub(r'\\D','',intl))}")
    try:
        import phonenumbers
        from phonenumbers import carrier, geocoder, number_type, PhoneNumberType
        num = phonenumbers.parse(intl)
        print(f"Valid (phonenumbers) : {phonenumbers.is_valid_number(num)}")
        print(f"Negara               : {geocoder.description_for_number(num, 'id') or '-'}")
        print(f"Operator (perkiraan) : {carrier.name_for_number(num, 'id') or '-'}")
        print(f"Seluler              : {number_type(num) in (PhoneNumberType.MOBILE, PhoneNumberType.FIXED_LINE_OR_MOBILE)}")
    except ImportError:
        print("Info lanjutan        : (install 'phonenumbers' untuk cek operator/negara: pip install phonenumbers)")

if __name__ == "__main__":
    main()
