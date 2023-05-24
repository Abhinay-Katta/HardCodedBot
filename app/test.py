from backend import HardCodedBot

bot = HardCodedBot()
for i in ['youtube', 'gmail', 'spotify']:
    bot.open_from_web(i)
