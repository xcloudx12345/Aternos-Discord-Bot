import os
from aternosapi import AternosAPI
import discord
from discord.ext import commands, tasks

headers_cookie = "ATERNOS_SEC_dpxjofznh7g00000=so8f6xmbeg000000; ATERNOS_LANGUAGE=vi; _ga=GA1.2.1312348077.1640397815; _gid=GA1.2.1121790510.1640397815; _pbjs_userid_consent_data=3524755945110770; _lr_env_src_ats=false; __gads=ID=8302d1106d2589c3-2295edb284cf00f2:T=1640397818:S=ALNI_MZNgB-u30d8gEqRh9yAky3dgXwKfQ; cto_bundle=6E8VAV9ZaTclMkJpZCUyRmsxVGxDJTJGcGx0RnpwMXlnS3BldmdHJTJCSXFzUWNGM3F1b25EVUZ3WVNsa1Q1azhkNXNraGRxUk55NmE1TzRwRzRlMWN6V1o4YmgzYmNJRjJKVnVRVCUyQmNCJTJGTXkzTW02eWF2emFIZkN5azVoTjBNZ3RlJTJCVE9LV1BhazJ3RDVCUyUy…t%2C%2025%20Dec%202021%2005%3A56%3A35%20GMT; _cc_id=6f35d5e59e306afa0e34553b0d1e8b4e; _pubcid_sharedid=01FQQNC3M78X9KGRXF8MWECKWB; _lr_retry_request=true; _gat=1; __cf_bm=roq.sDD_aeRldBR6YgCgwQH3jh2Wn6D9.xOtPHYGuXE-1640420955-0-AXU45i4FR3KfunN0bzqe0IUJ4aa2Irq3LTRvvokVaTw+pngOtSoHtX235Er6UGMdYTEi7qztTWjdQOSJay7UYcqKDVldtbRDeCAgvmvwVjYW+suKPOhk7Ld3XKjEZIp1hQ==; ATERNOS_SESSION=IC6BCH07JmhUlZakAwZ0vwWeQxpNPrjGiUCZCkkgeP7zfjNKAN8lz9vuDKoWg3v6Z1S4rL2hMu7svIw3UEJ2gMASD542pNZpBmPK; ATERNOS_SERVER=NpAiwwd2rk4EBV36"
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
    embed.add_field(name="start", value="Mở server.", inline=True)
    embed.add_field(name="stop", value="Tắt server.", inline=True)
    embed.add_field(name="status", value="Xem tình trạng server.", inline=True)
    embed.add_field(name="info", value="Thông tin server.", inline=True)
    embed.add_field(name="players", value="Xem số lượng người chơi.", inline=True)
    await ctx.send(embed = embed)

@client.command()
async def start(ctx):
    status = str(server.GetStatus())
    if (status == "Offline"):
        await ctx.send("Đang bắt đầu...")
        await cmd("start", ctx)
    else:
        await ctx.send("Server đang khởi động/đã chạy!")

@client.command()
async def stop(ctx):
    await ctx.send("Đang tắt...")
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
        await ctx.send("Không có ai online.")
        return
    for i in range(len(z)):
        await ctx.send(z[i])     
client.run(DISCORD)
