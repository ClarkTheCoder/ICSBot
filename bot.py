import discord
from discord.ext import commands
import random
from discord.voice_client import VoiceClient

startup_extensions = ["Music"]

TOKEN = 'NDkzNDY3NTMwNzE1NzI1ODM0.DolZuw.PwZoQtoXDnxtj81HAu0g1rHnr88'

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
	print('Bot is online.')

class Main_Commands():
	def __init__(self, bot):
		self.bot = bot

#commands
@bot.command()
async def flip():
	flip = random.choice(['heads', 'tails'])
	await bot.say(flip)

@bot.command(pass_context = 1)
async def roles(context):
	rolls = context.message.server.roles
	result = 'the roles are '
	for role in rolls:
		result += role.name + '. '
	await bot.say(result)

@bot.command(pass_context = 1)
async def num10(context):
	num = random.randint(1, 10)
	await bot.say(num)

#d2l
@bot.command(pass_context = 1)
async def d2l(context):
	d2lLogin = "https://online.camosun.ca/d2l/home"
	await bot.say(d2lLogin)

#ICS110 Outline
@bot.command(pass_context = 1)
async def ics110(context):
	ICS_110_Outline = "https://online.camosun.ca/d2l/le/content/138761/viewContent/2007132/View"
	await bot.say(ICS_110_Outline)

#ICS111 Outline
@bot.command(pass_context = 1)
async def ics111(context):
	ICS_111_Outline = "https://online.camosun.ca/d2l/le/content/139771/viewContent/2001972/View"
	await bot.say(ICS_111_Outline)

#ICS113 Outline
@bot.command(pass_context = 1)
async def ics113(context):
	ICS_113_Outline = "https://online.camosun.ca/d2l/le/content/139766/viewContent/2019362/View"
	await bot.say(ICS_113_Outline)

#ICS114 Outline
@bot.command(pass_context = 1)
async def ics114(context):
	ICS_114_Outline = "https://online.camosun.ca/d2l/le/content/139761/viewContent/2019493/View"
	await bot.say(ICS_114_Outline)

#learning skills Outline
@bot.command(pass_context = 1)
async def lrns(context):
	LRNS_Outline = "https://online.camosun.ca/d2l/le/content/139792/viewContent/2018333/View"
	await bot.say(LRNS_Outline)

#Pat's Math 155 Page
@bot.command(pass_context = 1)
async def math155(context):
	Math_155_Page = "http://wrean.ca/math155/"
	await bot.say(Math_155_Page)

#Pat's STATS 157 Page
@bot.command(pass_context = 1)
async def stats157(context):
	STATS_157_Page = "http://wrean.ca/stat157/"
	await bot.say(STATS_157_Page)

#music
if __name__ == "__main__":
	for extension in startup_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__, e)
			print('Failed to load extensions {}\n{}'.format(extension, exc))

#events
@bot.event
async def on_message(message):
	if message.content.upper().startswith('NIGGER'):
		await bot.send_message(message.channel, "Please do not use that word here.")

	await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    await bot.change_presence(game=discord.Game(name='Hi %s' % (member)))
    await bot.send_message(member, "Hi %s, Welcome to the Information and Computer Systems Discord Channel! Here you can share notes, discuss projects/due dates, receive support from other students, and just hang out. \n This server is not to be used for cheating/plagiarism or any other unetheical conduct. Please keep that in mind and enjoy your stay :) \n (I'm a bot in case that wasn't obvious. \n \n If you're familiar with Python, and you'd like to contribute check out my github repo: https://github.com/ClarkTheCoder/ICSBot" % (member))

@bot.event
async def on_member_remove(member):
    await bot.change_presence(game=discord.Game(name='Bye %s' % (member)))

#execute bot
bot.run(TOKEN)
