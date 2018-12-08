import discord
import asyncio
from random import randrange
from time import sleep
from threading import Thread
import os

money = discord.Client()
sending = False
channel = None
counter = 0

@money.event
async def on_ready():
	print( "Logged in." )

@money.event
async def on_message( msg ):
	global sending, counter, channel
	if msg.content.startswith( "f!start" ) and msg.author.id == "200335254282567680":
		sending = True
		channel = msg.channel
		await money.send_message( msg.channel, "->game multiple trivia 5" )
	elif msg.content.startswith( "f!stop" ) and msg.author.id == "200335254282567680":
		sending = False
		counter = 0
	elif msg.author.id == "213466096718708737" and msg.channel == channel and sending:
		if len( msg.embeds ) > 0:
			sleep( 2.5 )
			await money.send_message( msg.channel, str( randrange( 1, 3 ) ) )
		elif not msg.content.find( "That's not it, you have" ) == -1:
			sleep( 2.5 )
			await money.send_message( msg.channel, str( randrange( 3, 5 ) ) )
		elif not msg.content.find( "answering correctly!" ) == -1 or not msg.content.find( "ending game." ) == -1:
			counter += 1
			if counter == 5:
				sleep( 2.5 )
				counter = 0
				await money.send_message( msg.channel, "->game multiple trivia 5" )

money.run( os.getenv( "token", "" ), self_bot = True, bot = False )
