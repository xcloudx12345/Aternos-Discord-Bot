import os
from aternosapi import AternosAPI
import discord
from discord.ext import commands, tasks

headers_cookie = "ATERNOS_SEC_mqrmraiud8000000=c0pz41e4u6400000; ATERNOS_LANGUAGE=vi; __cf_bm=xIdRLMklWQlLpF0hLii1wb9Nm9vBaN6PEK83yJJjZfs-1640397786-0-ATkrCtee0bwR8N8hWZ7yJ32vV10VcehQmgucUOdDv6jgGi7NFdLT5QmXntYApFnumGiN58tvurbAiDatfBMPIiJ12SxcDkS7RxTU84SjsxmdrSHb8hKutqYUcrFVnquCdQ==; ATERNOS_SESSION=hKXn1P1djKuxSS4KApWCReL3cOE0geM2GaHtmNCJLr28b0fJJ7xoY2v5RXqEPBPxiIqtJUSWVPZmx75AI8HQdtjSVZI9BJIG1L9V; _ga=GA1.2.1312348077.1640397815; _gid=GA1.2.1121790510.1640397815; _pbjs_userid_consent_data=3524755945110770; _lr_retry_request=true; _lr_env_src_ats=false; __gads=ID=8302d1106d2589c3-2295edb284cf00f2:T=1640397818:S=ALNI_MZNgB-u30d8gEqRh9yAky3dgXwKfQ; cto_bundle=A3JD019QM05rYXR4aGhCZW1FU1NOZUVSUDhhdmc4bDh0cnc0OThwZVF6RHlRZHp6MzVmRFFQMnJPeFNTTFFRYmdkV20xTVV4YldtR1l5WVdicGVNeTRpMG9KSVh5RkM0enFBRSUyRnpSanVtWFo4VjRkTFk1M3EwUlhMZEZTazFsWkE2RXc0dWo2SzBnY1RadmdHVEZtZ1FVUVFVZyUzRCUzRA; ATERNOS_SERVER=NpAiwwd2rk4EBV36; cnx_userId=5dd4c1be057244b6b6c783f3b558d6aa; _pubcid=9b529ba3-049d-471f-8035-9b1a96702bb3; _pubcid_sharedid=01FQQNC3M78X9KGRXF8MWECKWB"
TOKEN = "hKXn1P1djKuxSS4KApWCReL3cOE0geM2GaHtmNCJLr28b0fJJ7xoY2v5RXqEPBPxiIqtJUSWVPZmx75AI8HQdtjSVZI9BJIG1L9V"
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
