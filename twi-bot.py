from telegram.ext import Updater,MessageHandler,Filters
ADAFRUIT_IO_USERNAME = "JOEL_V_J"
ADAFRUIT_IO_KEY = "aio_VJMD48I914RkPIrVxU2D51dRfrKg"
def lighton(bot,update):
  chat_id=bot.message.chat_id
  path=''
  Update.bot.sendPhoto(chat_id=chat_id,photo='https://static.scientificamerican.com/sciam/cache/file/2B38DE31-C1D3-4339-8808D61972976EE4.jpg')
  bot.message.reply_text("The light is on")
  from Adafruit_IO import Client
  aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
  aio.send('light',100)
  data = aio.receive('LIGHT')
  print('Received value: {0}'.format(data.value))
  
 def lightoff(bot,update):
  chat_id=bot.message.chat_id
  path=''
  Update.bot.sendPhoto(chat_id=chat_id,photo='https://image.shutterstock.com/image-photo/light-bulb-turned-off-over-260nw-162882104.jpg')
  bot.message.reply_text("The light is off")
  from Adafruit_IO import Client
  aio = Client('JOEL_V_J',ADAFRUIT_IO_KEY)
  aio.send('light',0)
  data = aio.receive('LIGHT')
  print('Received value: {0}'.format(data.value))
  
 def fanon(bot,update):
  chat_id=bot.message.chat_id
  path=''
  Update.bot.sendPhoto(chat_id=chat_id,photo='https://image.shutterstock.com/image-photo/ceiling-fan-rotating-room-electric-260nw-747740413.jpg')
  bot.message.reply_text("The fan is on")
  from Adafruit_IO import Client
  aio = Client('JOEL_V_J',ADAFRUIT_IO_KEY)
  aio.send('fan',100)
  data = aio.receive('FAN')
  print('Received value: {0}'.format(data.value))
  
  def fanoff(bot,update):
  chat_id=bot.message.chat_id
  path=''
  Update.bot.sendPhoto(chat_id=chat_id,photo='https://image.shutterstock.com/image-photo/black-ceiling-fan-on-white-260nw-1905057805.jpg')
  bot.message.reply_text("The fan is off")
  from Adafruit_IO import Client
  aio = Client('JOEL_V_J',ADAFRUIT_IO_KEY)
  aio.send('fan',0)
  data = aio.receive('FAN')
  print('Received value: {0}'.format(data.value))
  
  def greeting(bot,update):
    bot.message.reply_text("Hi,what can i do for you?")
    bot.message.reply_text("Commands only for light & fan")
    
    def demo(bot,update):
      a=bot.message.text
      a=a.lower()
      a=a.split()
      if 'light' in a and 'on'in a:
        lighton(bot,update)
        elif 'light' in a and 'off'in a:
        lightoff(bot,update)
       elif 'fan' in a and 'on'in a:
        fanon(bot,update)
         elif 'fan' in a and 'off'in a:
        fanoff(bot,update)
        elif 'hi' in a or 'hello' in a:
          greeting(bot,update)
         else:
          bot.message.reply_text("INVALID COMMAND")
          
          
          
          
          
          
          
          
BOT_TOKEN='1904744734:AAECMOiaZsG3GYRsYMmXNKFwK8Bz2oNrbUs'
u=Updater(BOT_TOKEN,use_context=True)
dp=u.dispatcher
dp.add_handler(MessageHandler(Filters.text,demo))
u.start_polling()
u.idle()
