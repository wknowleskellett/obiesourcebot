import sys

if len(sys.argv) < 2:
    print("python main.py <TOKEN ID>")
    sys.exit(1)

token = sys.argv[1]

import discord

bot = discord.Bot()

# --------------------
# COMMANDS
# --------------------

@bot.slash_command()
async def resources(ctx):
    await ctx.respond("resource stuff here")

@bot.slash_command()
async def hello(ctx, name: str = None, color: str = None):
    await ctx.respond(f"Hello, {name}! Your favorite color is {color}.")

bot.run(token)