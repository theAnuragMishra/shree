import hikari
import lightbulb

plugin = lightbulb.Plugin('misc')


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


@plugin.command
@lightbulb.command("misc", "Miscellaneous commands")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def misc_group(ctx: lightbulb.Context) -> None:
    pass


@misc_group.child
@lightbulb.command("rudrashtakam", "शिव रुद्राष्टकम")
@lightbulb.implements(lightbulb.SlashCommand)
async def rudrashtakam(ctx):
    await ctx.respond(
        "https://www.pdfnotes.co/wp-content/uploads/2021/09/shivrudra-min.png")
    await ctx.respond("https://open.spotify.com/track/3Z17nb1tjGCGGmWPVI9cHV?si=e500be2476cd496a")
    await ctx.respond("https://www.youtube.com/watch?v=m3m1dXmTrJU")
    await ctx.respond("https://www.wyo.in/pub/media/mf_webp/jpg/media/catalog/product/cache/718154c3aff62b1ad64160986aa81112/n/e/neon-adi-shiv-t-shirt-design-wyo-india.webp")
