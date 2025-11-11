import discord
from discord.ext import commands
import asyncio
import os
from config import BOT_TOKEN


class TalonOpsBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.guilds = True
        
        super().__init__(
            command_prefix='!',
            intents=intents,
            help_command=None
        )
    
    async def setup_hook(self):
        """Load all cogs"""
        cogs = [
            'cogs.team_registration',
            'cogs.team_management',
            'cogs.ringer_system',
            'cogs.scheduler',
            'cogs.pugs',
            'cogs.staff'
        ]
        
        for cog in cogs:
            try:
                await self.load_extension(cog)
                print(f'✅ Loaded {cog}')
            except Exception as e:
                print(f'❌ Failed to load {cog}: {e}')
        
        # Sync commands with Discord
        try:
            synced = await self.tree.sync()
            print(f'✅ Synced {len(synced)} command(s)')
        except Exception as e:
            print(f'❌ Failed to sync commands: {e}')
    
    async def on_ready(self):
        print(f'🤖 Bot is ready!')
        print(f'📝 Logged in as {self.user} (ID: {self.user.id})')
        print(f'🌐 Connected to {len(self.guilds)} guild(s)')
        print('─' * 50)


async def main():
    bot = TalonOpsBot()
    async with bot:
        await bot.start(BOT_TOKEN)


if __name__ == '__main__':
    asyncio.run(main())