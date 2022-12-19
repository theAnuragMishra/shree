import hikari
import lightbulb
import random

plugin = lightbulb.Plugin('Example')


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


@plugin.command
@lightbulb.command("shree_ram_aarti", "रामचन्द्र जी की आरती")
@lightbulb.implements(lightbulb.SlashCommand)
async def ram_aarti(ctx):
    # if ram_aarti.guild_id ==
    #     if ram_aarti.channel_id != "1054362555813994557":
    #         return
    await ctx.respond("https://open.spotify.com/track/6PyaU0ZWyBWtBLESuXYPA7?si=08bf61fa8a9b497e")
    await ctx.respond("https://www.youtube.com/watch?v=hMn3YQ5unR8")
    await ctx.respond("https://i.pinimg.com/564x/77/20/58/7720580af657dfdab78d863dde1a537f.jpg")
    await ctx.respond(
        "आरती कीजै श्री रघुवर जी की,\nसत चित आनन्द शिव सुन्दर की॥\n\nदशरथ तनय कौशल्या नन्दन,\nसुर मुनि रक्षक दैत्य निकन्दन॥\n\nअनुगत भक्त भक्त उर चन्दन,\nमर्यादा पुरुषोत्तम वर की॥\n\nनिर्गुण सगुण अनूप रूप निधि,\nसकल लोक वन्दित विभिन्न विधि॥\nहरण शोक-भय दायक नव निधि,\nमाया रहित दिव्य नर वर की॥\n\nजानकी पति सुर अधिपति जगपति,\nअखिल लोक पालक त्रिलोक गति॥\n\nविश्व वन्द्य अवन्ह अमित गति,\nएक मात्र गति सचराचर की॥\n\nशरणागत वत्सल व्रतधारी,\nभक्त कल्प तरुवर असुरारी॥\n\nनाम लेत जग पावनकारी,\nवानर सखा दीन दुख हर की॥")


@plugin.command
@lightbulb.command("rudrashtakam", "शिव रुद्राष्टकम")
@lightbulb.implements(lightbulb.SlashCommand)
async def ram_aarti(ctx):
    await ctx.respond("https://open.spotify.com/track/3Z17nb1tjGCGGmWPVI9cHV?si=e500be2476cd496a")
    await ctx.respond("https://www.youtube.com/watch?v=m3m1dXmTrJU")
    await ctx.respond("https://www.wyo.in/pub/media/mf_webp/jpg/media/catalog/product/cache/718154c3aff62b1ad64160986aa81112/n/e/neon-adi-shiv-t-shirt-design-wyo-india.webp")
    await ctx.respond(
        "नमामीशमीशान निर्वाणरूपं\nविभुं व्यापकं ब्रह्मवेदस्वरूपम्\nनिजं निर्गुणं निर्विकल्पं निरीहं\nचिदाकाशमाकाशवासं भजेहम्\n\nनिराकारमोङ्करमूलं तुरीयं\nगिराज्ञानगोतीतमीशं गिरीशम् ।\nकरालं महाकालकालं कृपालं\nगुणागारसंसारपारं नतोहम्\n\nतुषाराद्रिसंकाशगौरं गभिरं\nमनोभूतकोटिप्रभाश्री शरीरम् ।\nस्फुरन्मौलिकल्लोलिनी चारुगङ्गा\nलसद्भालबालेन्दु कण्ठे भुजङ्गा\n\nचलत्कुण्डलं भ्रूसुनेत्रं विशालं\nप्रसन्नाननं नीलकण्ठं दयालम् ।\nमृगाधीशचर्माम्बरं मुण्डमालं\nप्रियं शङ्करं सर्वनाथं भजामि\n\nप्रचण्डं प्रकृष्टं प्रगल्भं परेशं\nअखण्डं अजं भानुकोटिप्रकाशं ।\nत्र्यःशूलनिर्मूलनं शूलपाणिं\nभजेहं भवानीपतिं भावगम्यम्\nकलातीतकल्याण कल्पान्तकारी\nसदा सज्जनानन्ददाता पुरारी ।\nचिदानन्दसंदोह मोहापहारी\nप्रसीद प्रसीद प्रभो मन्मथारी\n\nन यावद् उमानाथपादारविन्दं\nभजन्तीह लोके परे वा नराणाम् ।\nन तावत्सुखं शान्ति सन्तापनाशं\nप्रसीद प्रभो सर्वभूताधिवासं\nन जानामि योगं जपं नैव पूजां\nनतोहं सदा सर्वदा शम्भुतुभ्यम् ।\nजराजन्मदुःखौघ तातप्यमानं\nप्रभो पाहि आपन्नमामीश शंभो")

