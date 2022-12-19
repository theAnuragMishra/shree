import hikari
import lightbulb

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('Discord_Token')

bot = lightbulb.BotApp(token=TOKEN, default_enabled_guilds=(947433833660317706,969951549650513960))

bot.load_extensions_from('./extensions')

bot.run()
