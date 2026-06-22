import os
import asyncio
import discord
from discord import app_commands
from discord.ext import commands
import yt_dlp
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user.name} online!")

@bot.tree.command(name="download", description="Zene letöltése MP3-ban")
async def download(interaction: discord.Interaction, link: str):
    await interaction.response.defer()
    
    filename = f"dl_{interaction.user.id}"
    mp3_path = f"{filename}.mp3"
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': filename,
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}],
        'quiet': True,
        'js_runtimes': {'node': {}}
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = await asyncio.to_thread(ydl.extract_info, link, download=True)
        
        title = info.get('title', 'Ismeretlen cím')
        uploader = info.get('uploader', 'Ismeretlen előadó')
        thumbnail = info.get('thumbnail')
        
        duration_sec = info.get('duration', 0)
        duration = f"{int(duration_sec // 60)}:{int(duration_sec % 60):02d}" if duration_sec else "Ismeretlen"

        embed = discord.Embed(title="Sikeres letöltés!", color=discord.Color.blue())
        embed.add_field(name="Cím", value=title, inline=False)
        embed.add_field(name="Előadó", value=uploader, inline=True)
        embed.add_field(name="Hossz", value=duration, inline=True)
        if thumbnail:
            embed.set_thumbnail(url=thumbnail)

        discord_file = discord.File(mp3_path, filename=f"{title}.mp3")
        await interaction.followup.send(embed=embed, file=discord_file)

    except Exception as e:
        print(f"HIBA: {e}")
        await interaction.followup.send(f"Hiba történt a letöltés során.")
    finally:
        if os.path.exists(mp3_path):
            os.remove(mp3_path)

bot.run(os.getenv("DISCORD_TOKEN"))