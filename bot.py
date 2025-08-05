import discord
from discord.ext import commands
from model import class_image 


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event 
async def on_ready():
    print("se inicio el bot")

@bot.command()
async def hola(ctx):    
    await ctx.send("Hola, como estas")  

@bot.command()
async def image(ctx):
    await ctx.send("Por favor, envía una imagen para analizar.")
    def verificar(mensaje):
        return mensaje.author == ctx.author and mensaje.channel == ctx.channel and len(mensaje.attachments) > 0

    mensaje = await bot.wait_for("message", check=verificar)
    imagen = mensaje.attachments[0]
    image_path = f"temp/{imagen.filename}"
    await imagen.save(image_path)
    model_path = "keras_model.h5"
    label_path = "labels.txt"
    clase = class_image(image_path, model_path, label_path)
    await ctx.send(f"La imagen es clasificada como: **{clase.strip()}**")

bot.run("MTMwNzExMzg3MjY3NDY1NjI1Ng.G4BkZ9.zsgEYKZ_GORc7Urweh2qJZd4uJ5Qke-PNgVuaI") 
