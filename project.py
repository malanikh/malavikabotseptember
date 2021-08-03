!pip install adafruit-io --quiet
# Import library and create instance of REST client.
from Adafruit_IO import Client
aio = Client('malavika001', 'aio_QgYq498GPemGVaXj9vVJB4zme0nc')
# Send the value 1 to a feed called 'Foo'.
aio.send('bedroom-dot-light',1)
aio.send('bedroom-dot-fan',1)
# Retrieve the most recent value from the feed 'Foo'.
# Access the value by reading the `value` property on the returned Data object.
# Note that all values retrieved from IO are strings so you might need to convert
# them to an int or numeric type if you expect a number.
data1 = aio.receive('bedroom-dot-light')
data2 = aio.receive('bedroom-dot-fan')
print(f'Received value: {data1.value}')
print(f'Received value: {data2.value}')
# Telegram
# https://python-telegram-bot.readthedocs.io/en/stable/


!pip install python-telegram-bot==13.0 --quiet
from telegram.ext import Updater,CommandHandler, MessageHandler,Filters 

def demo1(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://alumni.virginia.edu/learn/wp-content/uploads/sites/12/2018/11/light-bulb-in-dark.jpg'
  bot.message.reply_text('light turned on')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def demo2(bot,update):
  chat_id = bot.message.chat_id
  path = 'http://www.opportunitygrows.com/wp-content/uploads/2013/01/turn-off-lights.jpg'
  bot.message.reply_text('light turned off')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo3(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://www.warnerservice.com/hs-fs/hubfs/ceiling-fan.jpg?width=1000&name=ceiling-fan.jpg'
  bot.message.reply_text('fan turned on')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo4(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://thumbs.dreamstime.com/z/ceiling-fan-turned-off-111700139.jpg'
  bot.message.reply_text('fan turned off')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def main(bot,update):
  a = bot.message.text.lower()
  print(a)

  if a =="turn on light" or a=="light on":
    demo1(bot,update)
  elif a == "turn off light" or a=="light off":
    demo2(bot,update)
  elif a == "turn on fan" or a== "fan on":
    demo3(bot,update)
  elif a == "turn off fan" or a== "fan off":
    demo4(bot,update)
  else:
    bot.message.reply_text('Invalid Text')

BOT_TOKEN = '1946408078:AAE2uLq_34t1jSs1DN1Fi789ZbaqI01aEow'
u = Updater(BOT_TOKEN,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()

u.idle()
