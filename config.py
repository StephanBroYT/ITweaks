from disnake.ext import commands
import disnake

intents = disnake.Intents.all()
intents.members = True

bot = commands.Bot(
    command_prefix='/',
    intents=intents,
    activity=disnake.Game('Информирую о сервере'),
    status=disnake.Status.idle
    )

TOKEN = ''

OWNERS = [
    986355526948515870,
    986355526948515870
]

DevServers = 1146127100236026026