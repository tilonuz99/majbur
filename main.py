import telebot
import time
from telebot import types
import psycopg2
def newuser(message):
    try:
        connection = psycopg2.connect(user = "thzrixmbpxycue",
                                  password = "7184838441baf33aa0986afeca61e726ab610163a77c357087e3e826fc71fc5c",
                                  host = "ec2-54-210-128-153.compute-1.amazonaws.com",
                                  database = "d7tofl99vg7pq2")
        cursor = connection.cursor()
        sql_select_query = """select * from grs"""
        cursor.execute(sql_select_query)
        record = cursor.fetchall()
        if record not in message.from_user.id:
            sql_update_query = """INSERT INTO grs (grid, userid, kanal) VALUES (%s, %s, %s)"""
            cursor.execute(sql_update_query, (message.chat.id,message.from_user.id,''))
            
            bot.send_message(message.chat.id, "Bazaga yozildi")
        else:
            bot.send_message(message.chat.id, "avvaldan borsiz")
        sql_select_query = """select * from grs"""
        cursor.execute(sql_select_query)
        record = cursor.fetchall()
        connection.commit()
        
    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

username = "thzrixmbpxycue"
password = "7184838441baf33aa0986afeca61e726ab610163a77c357087e3e826fc71fc5c"
hostname = "gdt"
database = "d7tofl99vg7pq2"

connection = psycopg2.connect(user = "thzrixmbpxycue",
                                  password = "7184838441baf33aa0986afeca61e726ab610163a77c357087e3e826fc71fc5c",
                                  host = "ec2-54-210-128-153.compute-1.amazonaws.com",
                                  database = "d7tofl99vg7pq2")

bot = telebot.TeleBot("931190511:AAEuhHmrIiN5Lc_lNQq-ANjeauytWH2i5Gc")
restricted_messages = ["zzz", "zver"]

@bot.message_handler(commands=['add'])

def adddata(message):
    newuser(message)

@bot.message_handler(commands=['getdata'])
def getdata(message):
    msg = ""
    cursorr = connection.cursor()
    sql = "SELECT * FROM grs"
    cursorr.execute(sql)
    resultt = cursorr.fetchall()
    if resultt is None:
        bot.send_message(message.chat.id, "hech narsa yoq")
    else:
        for x in resultt:
            msg += "{}\n".format(x[0])
        bot.send_message(message.chat.id, msg)

@bot.inline_handler(lambda query: query.query == "Telegram")
def query_text(inline_query):
    r = types.InlineQueryResultArticle('1', 'Instagram', types.InputTextMessageContent('Instagramni bosdingiz'))
    r2 = types.InlineQueryResultArticle('2', 'Telegram', types.InputTextMessageContent('Telegramni bosdingiz'))
    bot.answer_inline_query(inline_query.id, [r, r2],cache_time=1)

@bot.message_handler(commands=['switch'])
def switch(message):
    markup = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text='Try', switch_inline_query="Telegram")
    markup.add(switch_button)
    bot.send_message(message.chat.id, "Chat turini tanlang", reply_markup=markup)

@bot.message_handler(commands=['start'])
def welcome(message):
    # Keyboard
    button_hi = types.KeyboardButton("Go")
    start_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_kb.add(button_hi)

    bot.send_message(message.chat.id, "Id {} Time: {}".format(message.from_user.id, time.time()), parse_mode='html',
                     reply_markup=start_kb)


@bot.message_handler(func=lambda msg: words_filter(msg, restricted_messages))
def set_ro(message):
    firstname = message.from_user.first_name
    chat_id = message.chat.id
    user_id = message.from_user.id
    bot.restrict_chat_member(chat_id, user_id, message.date + 600, False)
    bot.send_message(chat_id, "{} you have muted for an hour".format(firstname))


@bot.message_handler(content_types=['text'])
def lalala(message):
    button_next = types.KeyboardButton("davom etish")
    next_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    next_kb.add(button_next)
    if message.chat.type == 'private':
        if message.text == "Go":
            bot.send_message(message.chat.id, "Siz deaderuz kanaliga azo emassiz.", reply_markup=next_kb)
        elif message.text == 'davom etish':
            button_next2 = types.KeyboardButton("Ok")
            next_kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            next_kb2.add(button_next2)
            status = ['creator', 'administrator', 'member']
            for chri in status:
                if chri == bot.get_chat_member(chat_id="@deaderuz", user_id=message.chat.id).status:
                    bot.send_message(message.chat.id, "Azo boldingiz")
                    break
            else:
                bot.send_message(message.chat.id, "Azo bolmadingiz!")
        else:
            pass



# Filter for words
def words_filter(msg, words):
    if not msg.text:
        return False
    for word in words:
        if word in msg.text:
            return True
    return False


bot.polling(none_stop=True)
