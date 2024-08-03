import config

bot = config.bot

@bot.event
async def on_ready():
    bot.load_extension('cogs.profile')
    bot.load_extension('cogs.admin_tools')
    bot.load_extension('cogs.server')
    print(f'Бот активирован {bot.user.name} ({bot.user.id})')
    print('  ')
    print('  ')



# Bot creator's -> @Genes1us, @StephanBro_YT

bot.run(config.TOKEN)


