import telebot
import time
import psycopg2

def chek(message):
    connection = psycopg2.connect(user = "thzrixmbpxycue",
                                  password = "7184838441baf33aa0986afeca61e726ab610163a77c357087e3e826fc71fc5c",
                                  host = "ec2-54-210-128-153.compute-1.amazonaws.com",
                                  database = "d7tofl99vg7pq2")
    cursorr = connection.cursor()
    sql = "SELECT kanal FROM grs WHERE grid=message.chat.id"
    cursorr.execute(sql)
    resultt = cursorr.fetchone()
    if resultt is None:
    	return False
            
def getdata(message):
	chatid = message.chat.id
	msg = ""
	connection = psycopg2.connect(user = "thzrixmbpxycue",password = "7184838441baf33aa0986afeca61e726ab610163a77c357087e3e826fc71fc5c",host = "ec2-54-210-128-153.compute-1.amazonaws.com",database = "d7tofl99vg7pq2")
	cursorr = connection.cursor()
	cursorr.execute("SELECT kanal FROM grs WHERE grid=chatid")
	resultt = cursorr.fetchone()
	for x in resultt:
		msg += "{}".format(x[0])
	if msg is None:
		print("false")
	else:
		print("true")
            
def newchannel(message,chan):
    connection = psycopg2.connect(user = "thzrixmbpxycue",
                                  password = "7184838441baf33aa0986afeca61e726ab610163a77c357087e3e826fc71fc5c",
                                  host = "ec2-54-210-128-153.compute-1.amazonaws.com",
                                  database = "d7tofl99vg7pq2")
     
    msg = ""
    cursor = connection.cursor()
    sql_select_query = "SELECT kanal FROM grs"
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    for x in record:
        msg += "{}".format(x[0])
        fromid = str(chan)
    if  fromid not in msg:
        sql_update_query = """INSERT INTO grs (grid, userid, kanal) VALUES (%s, %s, %s)"""
        cursor.execute(sql_update_query, (message.chat.id,message.from_user.id,chan))
        bot.send_message(message.chat.id, "Guruhingiz kanalingizga ulandi.")
    else:
        sql_update_query = """Update mobile set kanal = %s where grid = %s"""
        cursor.execute(sql_update_query, (chan, message.chat.id))
        bot.send_message(message.chat.id, "Guruhingiz kanalingizga qayta ulandi.")
    
    connection.commit()

username = "thzrixmbpxycue"
password = "7184838441baf33aa0986afeca61e726ab610163a77c357087e3e826fc71fc5c"
hostname = "gdt"
database = "d7tofl99vg7pq2"

bot = telebot.TeleBot("931190511:AAEuhHmrIiN5Lc_lNQq-ANjeauytWH2i5Gc")

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, """Assalomu alaykum.""",parse_mode='html')


@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'supergroup':
		if  '/set' in message.text:
			channel=message.text.replace('/set ','').split(" ",1)[0]
			status = ['creator', 'administrator', 'member']
			for chri in status:
				if chri == bot.get_chat_member(chat_id=str(channel), user_id="@azoqilbot").status:
					newchannel(message,channel)
					break
				else:
					bot.send_message(message.chat.id, "Botni kanalga admin qilmadingiz.")


# Filter for words
def words_filter(msg, words):
    if not msg.text:
        return False
    for word in words:
        if word in msg.text:
            return True
    return False


bot.polling(none_stop=True)
