import os
from aternosapi import AternosAPI
import discord
from discord.ext import commands, tasks

headers_cookie = "ATERNOS_SEC_683plyxjyjh00000=5bgja1lshh300000; ATERNOS_LANGUAGE=en; _ga=GA1.2.1312348077.1640397815; _gid=GA1.2.1121790510.1640397815; _pbjs_userid_consent_data=3524755945110770; _lr_env_src_ats=false; __gads=ID=8302d1106d2589c3-2295edb284cf00f2:T=1640397818:S=ALNI_MZNgB-u30d8gEqRh9yAky3dgXwKfQ; cto_bundle=KC4nvF9HaXk4eSUyQkl2NnllZmNmb0hOd3klMkZBenRQU1BIYSUyQmtkUHVCeE85Q1AlMkZHMnNBUWRnYjhhVzdPR2dCOThYaDJ1bE1WMiUyQjM4VUZWVDlNZiUyQmN3aGJTJTJGdWNBUWUzM0pVYnpadDJIdldmdnNNdmxwQmglMkY4RkNrNTljdjJ3S2ZPSFZJcVNqJTJGdHJuVFpyMFJJTWxWTUI3OEFkZUElM0QlM0Q; cnx_userId=5dd4c1be057244b6b6c783f3b558d6aa; _pubcid=9b529ba3-049d-471f-8035-9b1a96702bb3; pbjs-unifiedid=%7B%22TDID%22%3A%22127b9edd-ab7f-4779-9d9d-764f37a91729%22%2C%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222021-12-25T05%3A39%3A07%22%7D; pbjs-unifiedid_last=Sat%2C%2025%20Dec%202021%2005%3A56%3A35%20GMT; _cc_id=6f35d5e59e306afa0e34553b0d1e8b4e; _pubcid_sharedid=01FQQNC3M78X9KGRXF8MWECKWB; ATERNOS_SESSION=IC6BCH07JmhUlZakAwZ0vwWeQxpNPrjGiUCZCkkgeP7zfjNKAN8lz9vuDKoWg3v6Z1S4rL2hMu7svIw3UEJ2gMASD542pNZpBmPK; ATERNOS_STYLE=dark; _gat=1; _lr_retry_request=true; __cf_bm=NzvwyZgyemmlBH3ieFBlYEzhvWw_B9.bqoSJIj.8ans-1640423113-0-Aft/oHv3iWE7ZPIIRPh9nOumb3PT6dZuXNWmfb3JU23LhRRn9XP3hYPZMbS1TgWTy234oa8d0b13Wbowdlj9pCJ8zsJ2XtSSfwr7nUhITD7L2RRx+ZlaIZxIuH9Bmx/tww==; ATERNOS_SERVER=NpAiwwd2rk4EBV36"
TOKEN = "wIoQFiuGXhKgQ6rmEkRX"
server = AternosAPI(headers_cookie, TOKEN, timeout=10)
DISCORD = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix = ["-"])
client.remove_command('help')

async def cmd(cmd, ctx):
    if cmd == "start":
        await ctx.send(server.StartServer())
    elif cmd == "stop":
        await ctx.send(server.StopServer())
    elif cmd == "status":
        await ctx.send(server.GetStatus())
    elif cmd == "info":
        await ctx.send(server.GetServerInfo())

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Watching over the SMP'))
    print('Initialized!')

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Current Commands", description="By Laxion", color=0x00ff00)
    embed.add_field(name="start", value="Starts the server.", inline=True)
    embed.add_field(name="stop", value="Stops the server.", inline=True)
    embed.add_field(name="status", value="Shows the current status of the server.", inline=True)
    embed.add_field(name="info", value="Shows server information.", inline=True)
    embed.add_field(name="players", value="Shows players information.", inline=True)
    await ctx.send(embed = embed)

@client.command()
async def start(ctx):
    status = str(server.GetStatus())
    if (status == "Offline"):
        await ctx.send("Starting...")
        await cmd("start", ctx)
    else:
        await ctx.send("Server is already starting/started!")

@client.command()
async def stop(ctx):
    await ctx.send("Stopping...")
    await cmd("stop", ctx)

@client.command()
async def info(ctx):
    await cmd("info", ctx)

@client.command()
async def status(ctx):
    await cmd("status", ctx)

@client.command()
async def players(ctx):
    z = server.GetPlayerInfo()
    if (len(z) == 0):
        await ctx.send("No players online.")
        return
    for i in range(len(z)):
        await ctx.send(z[i])     
client.run(DISCORD)
