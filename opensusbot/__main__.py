import os
from typing import Dict
import datetime

import discord
from discord.ext import commands

# Settings
NAME = os.environ.get("DISC_NAME") or "OpenSusBot"
COLOR = os.environ.get("DISC_COLOR") or 0xFF0000
SOURCE = os.environ.get("DISC_SOURCE") or "https://github.com/opensuspect/OpenSusBot"
FOOTER = os.environ.get("DISC_FOOTER") or "https://github.com/opensuspect/"
ICON = (
    os.environ.get("DISC_ICON")
    or "https://media.githubusercontent.com/media/"
    "opensuspect/opensuspect/main/misc/images/icon_1.png"
)

# Get discord secret key from environment variable
DISCORD_KEY: str = os.environ.get("DISCORD_KEY")
if DISCORD_KEY is None:
    raise ("No discord key supplied")

print(ICON)

client = commands.Bot(command_prefix="!")

def get_embed(
    title: str = None, 
    description: str = None, 
    fields: Dict = {}
) -> discord.Embed:

    embed = discord.Embed(title=title, description=description, color=COLOR)
    embed.set_author(name=NAME, url=SOURCE, icon_url=ICON)

    for key, value in fields.items():
        embed.add_field(name=key, value=value, inline=True)

    embed.set_footer(text=FOOTER)
    return embed


@client.event
async def on_ready():
    print(f"{NAME} is online.\n{SOURCE}")


@client.command()
async def ping(ctx):
    await ctx.send(
        embed=get_embed(
            fields={
                "Ping": str(round(client.latency * 1000)) + "ms",
                "Timestamp": int(datetime.datetime.now().timestamp()),
            }
        )
    )


def main() -> None:
    print("BLA:", DISCORD_KEY)
    client.run(DISCORD_KEY)
