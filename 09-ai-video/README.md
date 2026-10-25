# 🎬 09 — Tools AI Video

Video dari teks / foto, editing AI, sampai model open-source yang bisa jalan lokal.

## A. Generator Cloud (tanpa install, hasil paling bagus saat ini)

| Tool | Link Resmi | Terbaik Untuk | Gratis? |
|---|---|---|---|
| **Runway Gen-4.5** | https://runwayml.com | Produksi iklan/kreatif profesional + editor bawaan, kontrol kamera & motion | Kredit awal gratis, lalu berbayar |
| **Kling AI 3.0** | https://klingai.com | Sinematik hemat, gerak karakter & lip-sync kuat, klip s/d 15 dtk + audio native | Kredit harian gratis |
| **Google Veo 3.1 (Flow)** | https://labs.google/flow | Realistis + audio bawaan, lewat Google AI Pro/Ultra & Flow | Terbatas di paket Google AI |
| **OpenAI Sora 2** | https://sora.com | Text-to-video realistis, fisika & sinematik | Paket ChatGPT berbayar |
| **Luma Dream Machine (Ray3)** | https://lumalabs.ai | Image-to-video sinematik, preset kamera, keyframe | Paket berbayar (free tier lama sudah berubah) |
| **Pika 2.5** | https://pika.art | Konten sosial cepat + efek 1-klik (Pikaffects) | Free plan ada (watermark) |
| **Hailuo / MiniMax** | https://hailuoai.video | Gerak ekspresif, opsi hemat 1080p | Kredit trial |
| **Seedance (Dreamina)** | https://dreamina.capcut.com | Generator ByteDance, terintegrasi CapCut/Dreamina | Kredit trial |
| **PixVerse** | https://pixverse.ai | Video kreator pendek + audio | Kredit trial |
| **Adobe Firefly Video** | https://www.adobe.com/products/firefly.html | Kerja brand yang butuh lisensi & provenance jelas | Kredit di paket Adobe |

**Pilih cepat:** Profesional → Runway. Hemat & bagus → Kling. Realistis + suara → Veo 3.1. Efek lucu sosial → Pika. Di dalam CapCut → Seedance/Dreamina.

## B. Lokal / Open-Source (gratis, jalan di PC sendiri, butuh GPU)

| Tool / Model | Link Resmi | Catatan |
|---|---|---|
| **ComfyUI** | https://github.com/comfyanonymous/ComfyUI | Rumahnya workflow video lokal — pasang node Wan/Hunyuan/LTX di sini |
| **Wan 2.2 / Wan 2.6 (Alibaba)** | https://github.com/Wan-Video/Wan2.2 | Open-source favorit saat ini, text+image-to-video s/d 15 dtk |
| **HunyuanVideo (Tencent)** | https://github.com/Tencent-Hunyuan/HunyuanVideo | Open-source, kualitas tinggi, berat (VRAM besar) |
| **LTX-Video / LTX Studio** | https://ltx.io | Cepat & ringan dibanding model lain, ada versi studio cloud |
| **CogVideoX** | https://github.com/zai-org/CogVideo | Open-source, lebih ringan untuk GPU menengah |

> Jujur soal spek: PC tanpa GPU dedicated (atau VRAM <8GB) akan sangat lambat untuk video lokal. Untuk HP/PC ringan, jalur cloud di tabel A jauh lebih praktis.

## C. Pendukung Produksi Video AI

| Tool | Link | Fungsi |
|---|---|---|
| **CapCut Desktop** | https://www.capcut.com | Edit hasil AI, auto-caption, template TikTok/Reels |
| **DaVinci Resolve** | https://www.blackmagicdesign.com/products/davinciresolve | Editing + color grading profesional, versi gratis sangat lengkap |
| **Descript** | https://www.descript.com | Edit video lewat teks transkrip, hapus "ee.. um.." otomatis |
| **ElevenLabs** | https://elevenlabs.io | Voice-over AI / dubbing untuk narasi video |
| **Topaz Video AI** | https://www.topazlabs.com/topaz-video | Upscale & perhalus video (berbayar, trial ada) |

## D. Alur Kerja yang Paling Sering Dipakai
1. Tulis naskah & prompt adegan (bisa dibantu AI chat)
2. Generate per adegan 5–10 dtk di Kling / Runway / Veo
3. Voice-over di ElevenLabs (atau rekam sendiri + Audacity)
4. Rakit, caption, musik di CapCut / DaVinci Resolve
5. Upscale bila perlu di Topaz

## E. Tips Prompt Video
- Sebutkan: subjek + gerakan + gerakan kamera (`slow push-in`, `tracking shot`) + cahaya + gaya (`cinematic, 35mm`)
- 1 klip = 1 gerakan sederhana. Gerakan rumit sekaligus = hasil kacau.
- Pakai image-to-video kalau butuh wajah/produk konsisten — mulai dari foto yang bagus.
