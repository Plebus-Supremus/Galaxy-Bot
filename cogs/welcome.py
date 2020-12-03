# Imports
import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(id = 783631786575659028)

        if member.bot == True:
            role = discord.utils.get(member.guild.roles, name = 'Bots')
            await member.add_roles(role)

        else:
            role = discord.utils.get(member.guild.roles, name = 'Members')
            await member.add_roles(role)

            em = discord.Embed(title = f"Welcome to the Trident Galaxy, {member.name}!", description = f"Thanks for joining us {member.mention}! We are {len(list(member.guild.members))} members now!", color = 0x00ffff)
            em.set_thumbnail(url = 'https://cdn.discordapp.com/icons/724594864213196872/a_59895ada49e8d58f0b3abb76af8158be.gif?size=1024')
            em.add_field(name = "Top things to do here!", value = f"➣ First, read the rules from <#782969317746671656>\n\n➣ Then, take some ping roles from <#783547658081665064>\n\n➣ And then, you would be finally ready to make your home in <#783658211617406986>\n\n**Have fun and hope you don't leave us soon :D**")

            await channel.send(embed=em)
            await member.send(embed=em)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(id = 783631786575659028)

        em = discord.Embed(title = f"It seems like {member.name} just left us :pensive:", description = f"We are only {len(list(member.guild.members))} now :sob:", color = 0x00ffff)

        await channel.send(embed=em)

def setup(bot):
    bot.add_cog(Welcome(bot))
