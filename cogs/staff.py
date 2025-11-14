import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime
from config import BOT_LOGS_CHANNEL_ID


class Staff(commands.Cog):
    """Staff management and logging commands"""
    
    def __init__(self, bot):
        self.bot = bot
        self.log_buffer = [] # stores last 50 log entries for / log command, remove when Db?

    async def send_log(self, title: str, member: discord.Member):
        """
        Sends Embed to log channel
        """
        channel = self.bot.get_channel(BOT_LOGS_CHANNEL_ID)

        roles = [role.name for role in member.roles if role.name != "@everyone"] # Removes the @everyone role
        role_list =", ".join(roles) if roles else "No roles"

        embed = discord.Embed(
            title=title,
            color=discord.Color.orange(),
            timestamp=datetime.utcnow()
        )

        embed.add_field(name="User", value=f"{member} (ID: {member.id})", inline=False)
        embed.add_field(name="Nickname", value=member.nick if member.nick else "None", inline=False)
        embed.add_field(name="Roles", value=role_list, inline=False)

        await channel.send(embed=embed)

        self.log_buffer.append(f"{title}: {member} | Nickname: {member.nick} | Roles: {role_list}") # Save in the local cash
        if len(self.log_buffer) > 50:
            self.log_buffer.pop(0)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """
        Member joined server, runs send_log
        """
        await self.send_log("User oined the server", member)

    @commands.Cog.listener()
    async def on_member_revome(self, member: discord.Member):
        """
        Meber left server, runs send_log
        """
        await self.send_log("User left the server", member)

    


    @app_commands.command(name="logs", description="[STAFF] View bot activity logs")
    async def logs(self, interaction: discord.Interaction):
        """
        View recent logs, ephemeral msgs
        """
        if not self.logs_buffer:
            await interaction.response.send_message("No logs yet!", ephemeral = True)
            return
        text = "\n".join(self.log_buffer[-15:]) # Shows last 15 logs

        await interaction.response.send_message(
            f"```\n{text}\n```",
            ephemeral = True
        )
    
    @app_commands.command(name="cleanup", description="[STAFF] Run auto-cleanup for inactive teams/members")
    async def cleanup(self, interaction: discord.Interaction):
        pass
    
    @app_commands.command(name="force-disband", description="[STAFF] Force disband a team")
    async def force_disband(self, interaction: discord.Interaction):
        pass


async def setup(bot):
    await bot.add_cog(Staff(bot))
