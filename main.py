"""
Discord bot developed by Plebus Supremus#1234
Plebus Supremus (a.k.a Pleb) is also a verified bot developer with the verified bot being a bot named 'Trident'
Trident has been abandoned due to certain reasons that can't be said publicly.
Join our server if you get any errors or have any doubts, or want to contact with the developer. 
Link: https://discord.gg/6kTm5aH2fm
"""

# Imports
import discord
from discord.ext import commands
import os

# Declaring the bot variable
bot = commands.Bot(command_prefix = '.', help_command = None, case_insensitive = True, intents = discord.Intents.all())

# This event lets us know when the bot is ready
@bot.event
async def on_ready():
    print("Galaxy Bot is now ready!")

# Loading all the cogs
for x in os.listdir('./cogs'):
    if x.endswith('.py'):
        bot.load_extension(f"cogs.{x[:-3]}")

# Creating a dictionary of colors, so we can randomise the colors
bot.colors = {
  'WHITE': 0xFFFFFF,
  'AQUA': 0x1ABC9C,
  'GREEN': 0x2ECC71,
  'BLUE': 0x3498DB,
  'PURPLE': 0x9B59B6,
  'SPECIAL_PURPLE': 0xAD91FF,
  'LUMINOUS_VIVID_PINK': 0xE91E63,
  'GOLD': 0xF1C40F,
  'ORANGE': 0xE67E22,
  'RED': 0xE74C3C,
  'NAVY': 0x34495E,
  'DARK_AQUA': 0x11806A,
  'DARK_GREEN': 0x1F8B4C,
  'DARK_BLUE': 0x206694,
  'DARK_PURPLE': 0x71368A,
  'DARK_VIVID_PINK': 0xAD1457,
  'DARK_GOLD': 0xC27C0E,
  'DARK_ORANGE': 0xA84300,
  'DARK_RED': 0x992D22,
  'DARK_NAVY': 0x2C3E50,
  'SPECIAL_NAVY': 0x1D1E28
}

# Gets a randomised color from the list
bot.color_list = [c for c in bot.colors.values()]

# Make a folder named 'token' in the parent directory and then create a file in it called 'token.txt' and just copy and paste your bot token in it.
TOKEN = open('./token/token.txt').read()

# Running the bot
bot.run(TOKEN)
