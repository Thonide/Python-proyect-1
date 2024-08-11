import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def remove(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)

@bot.command()
async def multiplicate(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def divide(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left / right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def contaminacion_ambiental(ctx):
    await ctx.send(f"""Hola, soy {bot.user}, tu bot de confianza!""")
    await ctx.send(f'¿deseas saber un poco sobre la contaminacion ambiental?   "si" o "no" ')
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['sí', 'si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content in ['sí', 'si']:
            await ctx.send("La contaminacion ambiental es peligrosa, ya que esta dañando nuestros ecosistemas, algunos tipos de contaminacion ambiental son:")
            await ctx.send("1. acuatica: hay personas y fabricas que tiran sus desechos a los rios, mares o lagos lo cual provoca que el agua poco a poco se vuelva totalmente sucia si este problema continua no habra mas agua potable")   
            await ctx.send("2. aerea: los vehiculos que usan gasolina contaminan el aire provocando que la atmosfera se deteriore poco a poco, haciendo que los rayos solare golpeen la tierra más directamente")
            await ctx.send("3. terrestre: los desechos humanos como plastico, baterias y otros, contaminan el suelo y cuestan mucho de deshacerse por lo que se acumulan")
            await ctx.send("4. caza ilegal o furtiva: muchos animales como los pandas, ajolotes, pez gato, tiburon martillo, entre otros, se encuentran en peligro de extincion ya que quedan muy pocos de su especie")
        else:
            await ctx.send("comprendo, si alguna vez tienes una duda, no dudes en preguntarmelo.")
    else:
        await ctx.send("No te comprendo. ¿Me lo puedes repetir?")

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


bot.run('token')
