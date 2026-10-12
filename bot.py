import telebot
from telebot import types

TOKEN = "8848385861:AAG7eyDrwZtlTQo-Rs3zdPl7CaqYMbgEef8"
bot = telebot.TeleBot(TOKEN)

ETISALAT = "01131248353"

@bot.message_handler(commands=['start'])
def start(message):
    text = f"""🤖 أهلا بيك في Botify EG 🇪🇬
متجر بونات تليجرام #1 في مصر

💳 الدفع: اتصالات كاش فقط
📱 {ETISALAT}

👇 اختار الخدمة:"""
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🛒 متجر 15$", callback_data="store"),
        types.InlineKeyboardButton("🍽️ مطعم 20$", callback_data="rest"),
        types.InlineKeyboardButton("📁 ملفات 10$", callback_data="files"),
        types.InlineKeyboardButton("⭐ باقة 40$", callback_data="bundle")
    )
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "store":
        msg = f"🛒 بوت متجر 15$\nسلة + دفع\nحول على {ETISALAT} وابعت الاسكرين"
    elif call.data == "rest":
        msg = f"🍽️ بوت مطعم 20$\nمنيو + طلبات\nحول على {ETISALAT}"
    elif call.data == "files":
        msg = f"📁 بوت ملفات 10$\nبيع ملفات\nحول على {ETISALAT}"
    else:
        msg = f"⭐ باقة 40$\nكل البوتات + دعم شهر\nحول على {ETISALAT}"
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, msg)

print("Bot is running...")
bot.infinity_polling()