import hikari
import lightbulb
import asyncio

plugin = lightbulb.Plugin('chalisa')

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

@plugin.command
@lightbulb.command("chalisa", "All the chalisas!")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def chalisa_group(ctx: lightbulb.Context) -> None:
    pass

@chalisa_group.child
@lightbulb.command("hanuman_chalisa", "हनुमान चालीसा")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def chalisa_hanuman(ctx: lightbulb.Context) -> None:
    await ctx.respond(
        "https://cdntc.mpanchang.com/mpnc/images/lyrics/hanuman_chalisa_hi.jpg")
    await ctx.respond("https://open.spotify.com/track/6H7fLdt0AeWpuxUKXuXWrx")
    await ctx.respond("https://www.youtube.com/watch?v=AETFvQonfV8")
    
