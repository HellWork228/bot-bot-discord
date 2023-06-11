import discord
import os
import random
from discord.ext import commands
from advices import advice  
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}! Я могу подсказать интересные советы для улучшения экологии!')

@bot.command()
async def совет(ctx):
    await ctx.send(advice())

@bot.command()
async def картинка(ctx):
    images=(os.listdir('images'))
    img_name=random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("токен")
