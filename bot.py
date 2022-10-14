import nextcord 
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)

vragen = ['Wat is het verschil tussen int en str', 'A. String is een letter en int is een nummer', 'B. String is een nummer en int is een letter', 'C. String is een letter en int is een decimal getal']
optie = ['A', 'B', 'C']
antwoord = ['A']
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_member_join(ctx, member):
    await ctx.send(vragen[0], vragen[1], vragen[2], vragen[3])
    await bot.wait_for(optie)
    
bot.run()
