import hikari
import lightbulb

plugin = lightbulb.Plugin('chalisa')

def load(bot: lightbulb.Botapp) -> None:
    bot.add_plugin(plugin)

@plugin.command
@lightbulb.command("chalisa", "All the chalisas!")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def chalisa_group(ctx: lightbulb.Context) -> None:
    pass

@chalisa_group.child
@lightbulb.command("Hanuman_Chalisa", "हनुमान चालीसा")
@lightbulb.implements(lightbulb.SlashCommand)
async def chalisa_hanuman(ctx):
    await ctx.respond(
        "https://cdntc.mpanchang.com/mpnc/images/lyrics/hanuman_chalisa_hi.jpg")
    await ctx.respond("https://open.spotify.com/track/6H7fLdt0AeWpuxUKXuXWrx")
    await ctx.respond("https://www.youtube.com/watch?v=AETFvQonfV8")
    await ctx.respond("https://static.punjabkesari.in/multimedia/08_09_079750469hanuman-ji.jpg")
    