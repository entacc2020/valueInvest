from bot import telegram_chatbot
import os
import url
import valueinvest

bot = telegram_chatbot("config.cfg")

print("Server Running")


def make_reply(msg):
    if msg is not None:
        answer = valueinvest.browse(msg)
        #os.system("/usr/bin/python3 /home/shrihari/Desktop/javaScript/tools/valueInvest/valueinvest.py")
        # f = open("/home/shrihari/Desktop/javaScript/tools/telegramChatbox/itc ltd.txt" ,"r")
        # reply = f.read()
        answer = answer.replace('&', 'and')
        print(answer)
        
    return answer

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
            bot.send_message("Processing..." + message , from_)
            reply = make_reply(message)
            bot.send_message(reply, from_)
