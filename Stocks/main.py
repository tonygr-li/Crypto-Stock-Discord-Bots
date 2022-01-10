import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive 
from stocks import stock_info, stock_price, my_stocks

client = discord.Client()

# Help Stocks
def help_stocks():
  text_message = '''Hi I'm LIT, your friendly discord bot!!

Stocks:
  $stock price X = Gives its recent prices and open/close value
  $stock info X = Gives a full overview of its features
  If invalid symbol, please make sure it is capital or search its symbol online

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
  print("LIT Stock BOT is in " + str(guild_count) + " guilds.")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$stocks help'):
    help = help_stocks()
    await message.channel.send(help)

  if msg.startswith('$stocks tony'):
    tony_stock = my_stock()
    await message.channel.send(tony_stock)


  #Stock Price
  if msg.startswith("$stock price"):
    try:
      stock_name = msg.split("$stock price ",1)[1]
      get_price = stock_price(stock_name)
      await message.channel.send(get_price)
    except:
      print("Please enter a valid symbol or search it online (make sure it is capitalized)")

  #Stock Info
  if msg.startswith("$stock info"):
    try:
      stock_name = msg.split("$stock info ",1)[1]
      get_info = stock_info(stock_name)
      await message.channel.send(get_info)
    except:
      print("Please enter a valid symbol or search it online (make sure it is capitalized)")

#Server stuff
keep_alive()
my_secret = os.environ['TOKEN']
client.run(os.environ['TOKEN'])
