import random

import hikari
import lightbulb

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('Discord_Token')

bot = lightbulb.BotApp(token=TOKEN, default_enabled_guilds=(947433833660317706,969951549650513960))

bot.load_extensions_from('./extensions')

bot_status = random.choice(["Shree Ram Stuti", "the Hanuman Chalisa", "Shiv Tandav Strotam", "Rudrashtakam",])
bot.run(
    status=hikari.Status.ONLINE,
    activity=hikari.Activity(
        name=f"{bot_status}",
        type=hikari.ActivityType.LISTENING,
    ),
)

