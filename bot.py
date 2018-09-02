#Bot by italiano.amazing.exe
#If u modify this give credit to me
#For support the bot

import discord
import asyncio
import json
import os
from discord.ext import commands
from discord.ext.commands import Bot


bot = commands.Bot(command_prefix=';;;')
bot.remove_command('help')

@bot.event
async def on_ready():
    print ("Online Bot")
    print ("Mi sto preparando per andare online " + (bot.user.name))
    await bot.change_presence(game=discord.Game(name="Prefix ;;; | Versione 2.0", type=1))
    print ("Con l'id : " + (bot.user.id))

@bot.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Utente')
    await bot.add_roles(member, role)

@bot.command(pass_context=True)
async def echo(ctx, *, message):
    await bot.send_message(ctx.message.channel, message)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: Pong!! ")
    print ("User has pinged")

@bot.command(pass_context=True)
async def source(ctx):
    await bot.say("Source https://github.com/Bildcraft1/easy-bot ")
    print ("User ha guardato la source del bot")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{} Info".format(ctx.message.author.name), description="Qui ci sono le informazioni che ho trovato", color=0xff00b3)
    embed.add_field(name="Nome", value=ctx.message.author.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.author.id, inline=True)
    embed.add_field(name="Stato", value=ctx.message.author.status, inline=True)
    embed.add_field(name="Ruolo più alto", value=ctx.message.author.top_role)
    embed.add_field(name="Il Player è entrato il", value=ctx.message.author.joined_at)
    embed.set_thumbnail(url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{} info".format(ctx.message.server.name), description="Server info", color=0x00ff00)
    embed.set_author(name="italiano.amazing.exe")
    embed.add_field(name="Server name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Ruoli", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Membri", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in bot.log_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await bot.delete_message(messages)
    await bot.say('Messaggi Cancellati')


@bot.command(pass_context=True)
@commands.has_role("Mod")
async def kick (ctx, user: discord.Member):
    await bot.say(":boot: Cya {} Ya Loser!".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    await bot.say("``{} was banned``".format(user.name))
    await bot.ban(user)


@bot.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(title="This is a embed test", description="This is a really cool test", color=0x00ff00)
    embed.set_footer(text="This is embed footer")
    embed.set_author(name="italiano.amazing.exe")
    embed.add_field(name="This is a embed field", value="yes", inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.dark_green()
    )

    embed.set_author(name='Help')
    embed.add_field(name=';;;ping', value='Il Bot rispondera Pong', inline=False)
    embed.add_field(name=';;;kick <username>', value='Il Bot kickera l utente selezzionato ', inline=False)
    embed.add_field(name=';;;ban <username>', value='Il Bot bannera l utente selezzionato ', inline=False)
    embed.add_field(name=';;;echo <testo>', value='Il Bot ripetera il messaggio ', inline=False)
    embed.add_field(name=';;;info <username>', value='Il Bot farà vedere le info dell utente seleezzionato', inline=False)
    embed.add_field(name=';;;serverinfo', value='Il Bot farà vedere le info del server', inline=False)
    embed.add_field(name=';;;source', value='Il Bot farà vedere la source del bot', inline=False)
    embed.add_field(name='Bot Info', value='Versione 2.1 | Beta', inline=True)

    await bot.send_message(author, embed=embed)

@bot.command(pass_context=True)
async def opt(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.dark_green()
    )

    embed.set_author(name='opt')
    embed.add_field(name='OPT', value='Condor Spamma', inline=False)
    await bot.send_message(author, embed=embed)

bot.run("UR TOKEN")
