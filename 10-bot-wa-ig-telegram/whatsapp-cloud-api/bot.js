// WhatsApp Cloud API (RESMI Meta) — webhook server starter, Node.js + Express
// Alur daftar: developers.facebook.com -> WhatsApp -> nomor tes gratis tersedia.
// Token & nomor pengirim diambil dari dashboard app kamu. Semua rahasia di .env.
require('dotenv').config();
const express = require('express');
const app = express();
app.use(express.json());

const { VERIFY_TOKEN, WA_TOKEN, PHONE_NUMBER_ID } = process.env;

// 1) Verifikasi webhook (Meta memanggil GET ini sekali saat kamu daftarkan URL)
app.get('/webhook', (req, res) => {
  const { 'hub.mode': mode, 'hub.verify_token': token, 'hub.challenge': challenge } = req.query;
  if (mode === 'subscribe' && token === VERIFY_TOKEN) return res.status(200).send(challenge);
  return res.sendStatus(403);
});

// 2) Pesan masuk -> balas echo (hanya ke orang yang chat duluan: jendela 24 jam, sesuai aturan Meta)
app.post('/webhook', async (req, res) => {
  res.sendStatus(200); // jawab cepat dulu, proses di belakang
  try {
    const msg = req.body?.entry?.[0]?.changes?.[0]?.value?.messages?.[0];
    if (!msg || msg.type !== 'text') return;
    await fetch(`https://graph.facebook.com/v21.0/${PHONE_NUMBER_ID}/messages`, {
      method: 'POST',
      headers: { Authorization: `Bearer ${WA_TOKEN}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        messaging_product: 'whatsapp', to: msg.from,
        text: { body: `Halo! Kamu menulis: "${msg.text.body}"\n\n— dibalas otomatis oleh bot (WhatsApp Cloud API resmi)` },
      }),
    });
  } catch (e) { console.error(e); }
});

app.listen(process.env.PORT || 3000, () => console.log('Webhook WA jalan di port', process.env.PORT || 3000));
// Catatan aturan Meta: pesan promosi/broadcast WAJIB pakai template message yang disetujui,
// dan hanya ke user yang opt-in. Jangan spam — nomor bisa dibatasi/diblokir Meta.
