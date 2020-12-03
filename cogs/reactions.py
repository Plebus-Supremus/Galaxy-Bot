# Imports
import discord
from discord.ext import commands

class PingRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, reaction):
        if reaction.message_id == 783926029685227537:

            if str(reaction.emoji) == "📢":
                guild = self.bot.get_guild(reaction.guild_id)
                role = discord.utils.get(guild.roles, name = 'Announcements Ping')
                user = guild.get_member(reaction.user_id)
                await user.add_roles(role)

            if str(reaction.emoji) == "🎉":
                guild = self.bot.get_guild(reaction.guild_id)
                role = discord.utils.get(guild.roles, name = 'Giveaways Ping')
                user = guild.get_member(reaction.user_id)
                await user.add_roles(role)

            if str(reaction.emoji) == "✨":
                guild = self.bot.get_guild(reaction.guild_id)
                role = discord.utils.get(guild.roles, name = 'Events Ping')
                user = guild.get_member(reaction.user_id)
                await user.add_roles(role)

            if str(reaction.emoji) == "🔔":
                guild = self.bot.get_guild(reaction.guild_id)
                role = discord.utils.get(guild.roles, name = 'Updates')
                user = guild.get_member(reaction.user_id)
                await user.add_roles(role)

            if str(reaction.emoji) == "❤️":
                guild = self.bot.get_guild(reaction.guild_id)
                role = discord.utils.get(guild.roles, name = 'Chat Revival Ping')
                user = guild.get_member(reaction.user_id)
                await user.add_roles(role)

        elif reaction.message_id == 783926043806662657:
            if str(reaction.emoji) == '<a:greentick:783923665850204171>':
                guild = self.bot.get_guild(reaction.guild_id)
                user = guild.get_member(reaction.user_id)
                role1 = discord.utils.get(guild.roles, name = 'Announcements Ping')
                role2 = discord.utils.get(guild.roles, name = 'Giveaways Ping')
                role3 = discord.utils.get(guild.roles, name = 'Events Ping')
                role4 = discord.utils.get(guild.roles, name = 'Updates')
                role5 = discord.utils.get(guild.roles, name = 'Chat Revival Ping')
                await user.add_roles(role1)
                await user.add_roles(role2)
                await user.add_roles(role3)
                await user.add_roles(role4)
                await user.add_roles(role5)

            if str(reaction.emoji) == '<a:redcross:783923695122120704>':
                guild = self.bot.get_guild(reaction.guild_id)
                user = guild.get_member(reaction.user_id)
                role1 = discord.utils.get(guild.roles, name = 'Announcements Ping')
                role2 = discord.utils.get(guild.roles, name = 'Giveaways Ping')
                role3 = discord.utils.get(guild.roles, name = 'Events Ping')
                role4 = discord.utils.get(guild.roles, name = 'Updates')
                role5 = discord.utils.get(guild.roles, name = 'Chat Revival Ping')
                await user.remove_roles(role1)
                await user.remove_roles(role2)
                await user.remove_roles(role3)
                await user.remove_roles(role4)
                await user.remove_roles(role5)

        else:
            return

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, reaction):
        if reaction.message_id == 783926029685227537:

            if str(reaction.emoji) == "📢":
                guild = self.bot.get_guild(reaction.guild_id)
                role = discord.utils.get(guild.roles, name = 'Announcements Ping')
                user = guild.get_member(reaction.user_id)
                await user.remove_roles(role)

            if str(reaction.emoji) == "🎉":
                guild = self.bot.get_guild(reaction.guild_id)
                role = discord.utils.get(guild.roles, name = 'Giveaways Ping')
                user = guild.get_member(reaction.user_id)
                await user.remove_roles(role)

            if str(reaction.emoji) == "✨":
                guild = self.bot.get_guild(reaction.guild_id)
                role = discord.utils.get(guild.roles, name = 'Events Ping')
                user = guild.get_member(reaction.user_id)
                await user.remove_roles(role)

            if str(reaction.emoji) == "🔔":
                guild = self.bot.get_guild(reaction.guild_id)
                role = discord.utils.get(guild.roles, name = 'Updates')
                user = guild.get_member(reaction.user_id)
                await user.remove_roles(role)

            if str(reaction.emoji) == "❤️":
                guild = self.bot.get_guild(reaction.guild_id)
                role = discord.utils.get(guild.roles, name = 'Chat Revival Ping')
                user = guild.get_member(reaction.user_id)
                await user.remove_roles(role)

        else:
            return

    @commands.command()
    @commands.has_role('Owner')
    async def rr(self, ctx):
        embed = discord.Embed(title = "Ping Roles!", color = 0xeb3449)
        role1 = discord.utils.get(ctx.guild.roles, name = 'Announcements Ping')
        role2 = discord.utils.get(ctx.guild.roles, name = 'Giveaways Ping')
        role3 = discord.utils.get(ctx.guild.roles, name = 'Events Ping')
        role4 = discord.utils.get(ctx.guild.roles, name = 'Updates')
        role5 = discord.utils.get(ctx.guild.roles, name = 'Chat Revival Ping')
        embed.add_field(name = "📢 Announcements!", value = f"**• Usage:** You will be pinged whenever there is an announcement to be made.\n**• Estimated:** 2-3 times a week\n**• Role:** {role1.mention}", inline = False)
        embed.add_field(name = "🎉 Giveaways!", value = f"**• Usage:** You will be pinged whenever there is a giveaway hosted.\n**• Estimated:** 1 time every couple of days\n**• Role:** {role2.mention}", inline = False)
        embed.add_field(name = "✨ Events!", value = f"**• Usage:** You will be pinged whenever there is an event hosted.\n**• Estimated:** 1-2 times every fortnight\n**• Role:** {role3.mention}", inline = False)
        embed.add_field(name = "🔔 Updates!", value = f"**• Usage:** You will be pinged whenever an update is made to the server or my bots.\n**• Estimated:** 1-2 times every day\n**• Role:** {role4.mention}", inline = False)
        embed.add_field(name = "❤️ Chat Revival!", value = f"**• Usage:** You will be pinged whenever the chat is inactive and needs to be made active.\n**• Estimated:** 1-2 times every day\n**• Role:** {role5.mention}", inline = False)
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/783252386126626836/783363313416273950/Trident_Galaxy_Rules.png')
        
        channel = self.bot.get_channel(id = 783547658081665064)
        msg = await channel.send(embed=embed)

        await msg.add_reaction('📢')
        await msg.add_reaction('🎉')
        await msg.add_reaction('✨')
        await msg.add_reaction('🔔')
        await msg.add_reaction('❤️')

        mbed = discord.Embed(title = "Special Reactions!", description = "React with <a:greentick:783923665850204171> to get all the ping roles listed above!\n\nReact with <a:redcross:783923695122120704> to get all the ping roles that you have removed!", color = 0x00ffff)
        msg_ = await channel.send(embed=mbed)

        await msg_.add_reaction('<a:greentick:783923665850204171>')
        await msg_.add_reaction('<a:redcross:783923695122120704>')

def setup(bot):
    bot.add_cog(PingRoles(bot))
