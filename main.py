from pyrogram import Client, filters

# =========================
# DATA TELEGRAM API
# =========================

API_ID = 123456
API_HASH = "ISI_API_HASH"
BOT_TOKEN = "ISI_BOT_TOKEN"

# =========================
# MEMBUAT BOT
# =========================

app = Client(
    "botku",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# =========================
# SAAT ADA PESAN MASUK
# =========================

@app.on_message(filters.text)
async def balas_pesan(client, message):

    teks = message.text.lower()

    print("Pesan masuk:", teks)

    # SEARCHING KATA
    if "halo" in teks:
        await message.reply("Hai juga 👋")

    elif "makan" in teks:
        await message.reply("Kamu lapar ya 🍜")

    elif "siapa kamu" in teks:
        await message.reply("Aku bot Telegram kecil 🤖")

    else:
        await message.reply("Aku tidak mengerti 😭")

# =========================
# MENJALANKAN BOT
# =========================

print("Bot sedang berjalan...")

app.run()
