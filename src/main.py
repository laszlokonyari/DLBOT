import os
import asyncio
import discord
from discord import app_commands
from discord.ext import commands
import yt_dlp
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

def ytdl_download(url, output):
    opts = {
        'format': 'bestaudio/best',
        'outtmpl': output,
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}],
        'quiet': True
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user.name} online!")

@bot.tree.command(name="download", description="Zene letöltése MP3-ban")
async def download(interaction: discord.Interaction, link: str):
    await interaction.response.defer()
    
    mp3_path = f"dl_{interaction.user.id}.mp3"
    
    try:
        await asyncio.to_thread(ytdl_download, link, mp3_path.replace('.mp3', ''))
        
        await interaction.followup.send(file=discord.File(mp3_path))
    except Exception:
        await interaction.followup.send("Hiba történt a letöltés során.")
    finally:
        if os.path.exists(mp3_path):
            os.remove(mp3_path)

bot.run(os.getenv("DISCORD_TOKEN"))