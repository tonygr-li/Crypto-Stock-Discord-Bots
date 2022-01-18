import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive 
from crypto import symbol, price, coin, price_noname, my_crypto
from discord.ext import tasks

client = discord.Client()

#Help / Guide on Bot

# Help Crypto
def help_crypto():
  text_message = '''Hi I'm LIT, your friendly discord bot!!

Crypto:
  $crypto symbols = List symbols of coins and tokens
  $crypto info X = Info about X including high, low, bid, ask, price
  $crypto price X = Current price + 24h % of X

To suggest new features, or ask questions, please message my owner
  '''
  return(text_message)




#Verify Bot is working
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
  guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
  for guild in client.guilds:
		# PRINT THE SERVER'S ID AND NAME.
    print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
    guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
  print("LIT BOT is in " + str(guild_count) + " guilds.")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  #Bot guide 
  if msg.startswith('$crypto help'):
    help = help_crypto()
    await message.channel.send(help)


  #Crypto
  if msg.startswith('$crypto tony'):
    tony_crypto = my_crypto()
    await message.channel.send(tony_crypto)

  if msg.startswith('$crypto symbols'):
    crypto_symbols = symbol()
    await message.channel.send(crypto_symbols)

  if msg.startswith("$crypto price"):
    coin_name = msg.split("$crypto price ",1)[1]
    get_price = price(coin_name)
    await message.channel.send(get_price)

  if msg.startswith("$crypto info"):
    coin_name = msg.split("$crypto info ",1)[1]
    get_coin = coin(coin_name)
    await message.channel.send(get_coin)

#Server stuff
keep_alive()
my_secret = os.environ['TOKEN']
client.run(os.environ['TOKEN'])