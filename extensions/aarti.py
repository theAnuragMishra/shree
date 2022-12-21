import hikari
import lightbulb
import random
import asyncio

plugin = lightbulb.Plugin('aarti')


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


@plugin.command
@lightbulb.command("aarti", "All the aartis!")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def aarti_group(ctx: lightbulb.Context) -> None:
    pass


@aarti_group.child
@lightbulb.command("shree_ram", "रामचन्द्र जी की आरती")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def aarti_ram(ctx: lightbulb.Context) -> None:
    # if ram_aarti.guild_id ==
    #     if ram_aarti.channel_id != "1054362555813994557":
    #         return
    await ctx.respond(
        "https://hindiswaraj.com/wp-content/uploads/2021/04/Lord-Raghuvar-Aarti.jpg")
    await ctx.respond("https://open.spotify.com/track/6PyaU0ZWyBWtBLESuXYPA7?si=08bf61fa8a9b497e")
    await ctx.respond("https://www.youtube.com/watch?v=hMn3YQ5unR8")
