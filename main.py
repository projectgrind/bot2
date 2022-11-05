# Import the command handler
import lightbulb
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
from datetime import date
from datetime import datetime

now = datetime.now()

t = now.strftime("%H:%M:%S")
timestamp = date.fromtimestamp(1326244364)

time1=str(t)

time = str(timestamp)

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("key.json", scope)
client = gspread.authorize(creds)
sheet = client.open('record')
python_sheet = sheet.get_all_records()
pp = pprint.PrettyPrinter()

python_sheet=str(python_sheet )

# Instantiate a Bot instance
bot = lightbulb.BotApp(token="MTAzNTE4MDIwMTgyODcwMDE2MA.G90HVC.Z_T4HbbPQTNtp7uWF0QAEloGx9whFg0dhOvVOg", prefix="$")

# Register the command to the bot
@bot.command
# Use the command decorator to convert the function into a command
@lightbulb.command("ping", "checks the bot is alive")
# Define the command type(s) that this command implements
@lightbulb.implements(lightbulb.SlashCommand)
# Define the command's callback. The callback should take a single argument which will be
# an instance of a subclass of lightbulb.context.Context when passed in
async def ping(ctx: lightbulb.Context) -> None:
    # Send a message to the channel the command was used in
    await ctx.respond(f"Pong! {bot.heartbeat_latency * 1_000:.0f}ms")

@bot.command
@lightbulb.command("hello", "hello")
# Define the command type(s) that this command implements
@lightbulb.implements(lightbulb.SlashCommand)
# Define the command's callback. The callback should take a single argument which will be
# an instance of a subclass of lightbulb.context.Context when passed in
async def ping(ctx: lightbulb.Context) -> None:
    # Send a message to the channel the command was used in
    await ctx.respond("HELLO")

@bot.command
@lightbulb.command("instagram", " instagram link ")
# Define the command type(s) that this command implements
@lightbulb.implements(lightbulb.SlashCommand)
# Define the command's callback. The callback should take a single argument which will be
# an instance of a subclass of lightbulb.context.Context when passed in
async def ping(ctx: lightbulb.Context) -> None:
    # Send a message to the channel the command was used in
    await ctx.respond("instagram : https://www.instagram.com/theprojectgrind/ ")

@bot.command
@lightbulb.command("youtube", " youtube link ")
# Define the command type(s) that this command implements
@lightbulb.implements(lightbulb.SlashCommand)
# Define the command's callback. The callback should take a single argument which will be
# an instance of a subclass of lightbulb.context.Context when passed in
async def ping(ctx: lightbulb.Context) -> None:
    # Send a message to the channel the command was used in
    await ctx.respond("instagram : https://www.youtube.com/channel/UCHG5qAwYdc_SjIoBD5wpJYA")

@bot.command
@lightbulb.command("youtube", " youtube link ")
# Define the command type(s) that this command implements
@lightbulb.implements(lightbulb.SlashCommand)
# Define the command's callback. The callback should take a single argument which will be
# an instance of a subclass of lightbulb.context.Context when passed in
async def ping(ctx: lightbulb.Context) -> None:
    # Send a message to the channel the command was used in
    await ctx.respond("instagram : https://www.youtube.com/channel/UCHG5qAwYdc_SjIoBD5wpJYA")

@bot.command
@lightbulb.command("Records", " POSTING NEW VIDEO AND RECORD")
# Define the command type(s) that this command implements
@lightbulb.implements(lightbulb.SlashCommand)
# Define the command's callback. The callback should take a single argument which will be
# an instance of a subclass of lightbulb.context.Context when passed in
async def ping(ctx: lightbulb.Context) -> None:
    sheet = client.open('record').sheet1
    # Send a message to the channel the command was used in
    await ctx.respond(python_sheet)

bot.run()

