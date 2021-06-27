import telebot
api_key='1840659837:AAHZVf6NMyZr7kW8bMaGAwX8aR7-CLVWw28'
bot=telebot.TeleBot(api_key)
@bot.message_handler(content_types="text")
def ai(message):
   # print(message)
    if (message.text=="hi"):
        try:
            bot.reply_to(message,"hi how are you "+message.from_user.first_name+" "+message.from_user.last_name)
        except:
            bot.reply_to(message,"hi how are you "+message.from_user.first_name)
@bot.message_handler(content_types=["video"])
def hello(message):
    file_info = bot.get_file(message.video.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    bot.send_video(message.chat.id,data=downloaded_file,caption="sahil is great")
    bot.delete_message(chat_id=message.chat.id,message_id=message.message_id)
#print("hello world")