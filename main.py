import telebot
import os
from flask import Flask, request
api_key='1840659837:AAHZVf6NMyZr7kW8bMaGAwX8aR7-CLVWw28'
bot=telebot.TeleBot(api_key,parse_mode="none")
server = Flask(__name__)
@bot.message_handler(content_types="text")
def ai(message):
    print(message)
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
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://newnoob7.herokuapp.com/' + api_key)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))