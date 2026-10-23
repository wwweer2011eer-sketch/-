import os
from flask import Flask
from threading import Thread
import telebot
import random

TOKEN = os.environ.get("BOT_TOKEN", "")
bot = telebot.TeleBot(TOKEN)

app = Flask('')
@app.route('/')
def home():
    return "البوت شغال - لعيون فطومتي"
def run():
  app.run(host='0.0.0.0',port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

# --- الشعر ---
كل_الاشعار = [
    "انتي من تمشين يمشي وياج نهر\n- سمير صبيح",
    "عيونج عسل بس العسل مرات يمرمر\n- سمير صبيح",
    "من شفتها كمت اهذي\nكلت هاي منين؟ من يا كوكب؟\n- حسين الدليهمي",
    "ضحكتها ترد الروح\n- حسين الدليهمي",
    "يا حريمة انباكت الجلمات من فمّج\n- عريان السيد خلف",
    "القمر يغار من وجهج، والورد يتعلم من خدودج",
    "شعرج ليل وطول الليل اغار\nوجهج صبح وما اريد نهار",
    "عيونج حكاية لو قريتها ما اخلص",
    "فطومتي يا حلوة يا وردة البستان\nيا عطر يا نغمة يا الحان"
]

بدايات = ["فطومتي", "عيون فطومتي", "ضحكة فطومتي", "جمال فطومتي"]
اوصاف = ["جنة", "قمر", "وردة", "قصيدة", "حكاية", "عسل"]
تشابيه = ["ما اله مثيل", "يخبل", "يذوب الكلب", "لو شافها القمر يستحي"]
حب = ["احبج", "اموت عليج", "اعشقج فطومتي"]

def كلام_فطومة():
    if random.random() > 0.3:
        return random.choice(كل_الاشعار) + " ❤️"
    else:
        return f"{random.choice(بدايات)} {random.choice(اوصاف)} {random.choice(تشابيه)}، {random.choice(حب)} ❤️"

كلمات_الحب = ["احبه", "احبك", "اموت عليه", "اعشقه", "احب علي", "احب علاوي"]

# --- الازرار ---
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(KeyboardButton("لعيون فطومتي ❤️"))

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "هلا بفطومتي 👑\nدوسي على الزر جوه حتى يبدي الغزل", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text in ["لعيون فطومتي ❤️", "لعيون فطومتي"])
def لعيون_فطومة(message):
    bot.send_message(message.chat.id, f" علاوي يحبج يا فطومةي ❤️\n\n{كلام_فطومة()}", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def reply(message):
    if any(k in message.text.lower() for k in كلمات_الحب):
        bot.send_message(message.chat.id, "البت بس مو بكد حب علاوي الج يا فطومتي 😌❤️", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, كلام_فطومة(), reply_markup=markup)

keep_alive()
bot.infinity_polling()
