import discord
from discord import app_commands
from discord.ext import commands


class TeamRegistration(commands.Cog):
    """Handles team registration and verification"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="registerteam", description="Register a new team for the league")
    async def register_team(self, interaction: discord.Interaction):
        pass
    
    @app_commands.command(name="verify-team", description="[STAFF] Verify a pending team registration")
    async def verify_team(self, interaction: discord.Interaction):
        pass
    
    @app_commands.command(name="reject-team", description="[STAFF] Reject a pending team registration")
    async def reject_team(self, interaction: discord.Interaction):
        pass
    
    @app_commands.command(name="pending-teams", description="[STAFF] View all pending team registrations")
    async def pending_teams(self, interaction: discord.Interaction):
        pass


async def setup(bot):
    await bot.add_cog(TeamRegistration(bot))
