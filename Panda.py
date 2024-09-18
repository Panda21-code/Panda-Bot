import os
import discord
from discord.ext import commands
from discord import app_commands

from PandaServer import server_on

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())





# //////////////////// Bot Event ////////////////////
# คำสั่ง bot พร้อมใช้งานแล้ว
@bot.event
async def on_ready():
    print("Bot Online!")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")
    
    
    
    
# แจ้งคนเข้า -ออกเชิฟเวอร์
    
@bot.eventa
async def on_member_join(member):
    channel = bot.get_channel(1286055800992960677) # IDห้อง
    text = f"Welcome to the server, {member.mention}!"
    
    emmbed = discord.Embed(title = 'Welcome to the server!',
                           description = text,
                           color = 0x66FFFF)
    
    await channel.send(text) # ส่งข้อความไปที่ห้องนี้
    await channel.send(embed = emmbed) # ส่ง Embed ไปที่ห้องนี้
    await member.send(text) # ส่งข้อความไปที่แชทส่วนตัวของ member
    
    
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1286055800992960677) # IDห้อง
    text = f"{member.name} has left server!"
    await channel.send(text) # ส่งข้อความไปที่ห้องนี้
    
    
    
# คำสั่ง chatbot
@bot.event
async def on_message(message):
    mes = message.content # ดึงข้อความถูกส่งมา
    if mes == 'hello':
        await message.channel.send("Hello It's me") # ส่งกลับไปที่ห้องนั้น
        
    elif mes == 'hi bot':
        await message.channel.send("Hello, " + str(message.author.name))
        
    await bot.process_commands(message)
    # ทำคำสั่ง event แล้วไปทำคำสั่ง bot command ต่อ
    
    
    
    
# //////////////////// Commands ////////////////////
# กำหมดคำสั่งให้บอท

@bot.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx.author.name}!")
    
    
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
    
    
# Slash Commands
@bot.terr.command(name='hellobot',description='Replies with Hello')
async def hellocommand(interaction):
    await interaction.response.send_message("Hello It's me BOT DISCORD")


@bot.tree.command(name='name')
@app_commands.describe(name = "What's your name?")
async def namecommand(interaction, name : str):
    await interaction.response.send_message(f"Hello {name}")
    
    
# Embeds

@bot.tree.command(name='help', description='Bot commands')
async def helpcommand(interactuion):
    emmbed = discord.Embed(title='Help Me! - Bot Commands',
                           description='Bot Commands',
                           color=0x66FFFF,
                           timestamp= discord.utils.utcnow())
    
    
server_on()

bot.run(os.getenv('TOKEN'))
