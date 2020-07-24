from bot import telegram_chatbot
import os

bot = telegram_chatbot("config.cfg")

print("Server Running")


def make_reply(msg):
    reply = None
    if msg is not None:
        f = open("/home/shrihari/Desktop/javaScript/tools/jobs/output.txt","r")
        reply = f.read()
    return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            bot.send_message("Processing...", from_)
            reply = make_reply(message)
            bot.send_message(reply, from_)