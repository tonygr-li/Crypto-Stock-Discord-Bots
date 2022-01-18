import requests, json

def symbol():
  base_url = "https://api.gemini.com/v1"

  response = requests.get(base_url + "/symbols")
  symbols = response.json()

  return(symbols)
  
def price(name):
  base_url = "https://api.gemini.com/v1"
  response = requests.get(base_url + "/symbols")
  symbols = response.json()
  if name.lower() in symbols:
    base_url = "https://api.gemini.com/v1"
    full_url = "/pricefeed/" + str(name)
    response = requests.get(base_url + full_url)
    prices = response.json()

    coin = "Coin: " + prices[0].get("pair")
    current_price = "Current price: " + prices[0].get("price")
    percentage = "24h percentage: " + prices[0].get("percentChange24h")
    text = coin + "\n" + current_price + "\n" + percentage
    return text
  else:
    error_message = "Please enter a valid symbol or use $crypto symbols for a list"
    return error_message

def price_noname(name):
  base_url = "https://api.gemini.com/v1"
  response = requests.get(base_url + "/symbols")
  symbols = response.json()
  if name.lower() in symbols:
    base_url = "https://api.gemini.com/v1"
    full_url = "/pricefeed/" + str(name)
    response = requests.get(base_url + full_url)
    prices = response.json()

    current_price = "Current price: " + prices[0].get("price")
    percentage = "24h percentage: " + prices[0].get("percentChange24h")
    text = "\n" + current_price + "\n" + percentage
    return text
  else:
    error_message = "Please enter a valid symbol"
    return error_message

def coin(name):
  base_url = "https://api.gemini.com/v1"
  response = requests.get(base_url + "/symbols")
  symbols = response.json()
  if name.lower() in symbols:
    base_url = "https://api.gemini.com/v2"
    full_url = "/ticker/" + str(name)
    response = requests.get(base_url + full_url)
    coin_data = response.json()
    coin = "Coin: " + coin_data.get("symbol")
    price_24 = "24 hours ago: " + coin_data.get("open")
    high_24 = "High 24h: " + coin_data.get("high")
    low_24 = "Low 24h: " + coin_data.get("low")
    recent = "Recent trade: " + coin_data.get("close")
    bid = "Current bid: " + coin_data.get("bid")
    ask = "Current ask: " + coin_data.get("ask")

    text = coin + "\n" + recent + "\n" + high_24 + "\n" + low_24 + "\n" + recent + "\n" + bid + "\n" + ask
    return text
  else:
    error_message = "Please enter a valid symbol or use $crypto symbols for a list"
    return error_message


def my_crypto():
  btc = coin("BTCUSD") + price_noname("BTCUSD")
  eth = coin("ETHUSD") + price_noname("ETHUSD")
  doge = coin("DOGEUSD") + price_noname("DOGEUSD")
  ltc = coin("LTCUSD") + price_noname("LTCUSD")
  # rvn = coin("RVNUSD") + price_noname("RVNUSD")
  # xrp = coin("XRPUSD") + price_noname("XRPUSD")
  ftm = coin("FTMUSD") + price_noname("FTMUSD")
  grt = coin("grtusd") + price_noname("grtusd")
  

  text = btc + "\n\n" + eth + "\n\n" + doge + "\n\n" + ltc + "\n\n" + ftm + "\n\n" + grt
  return text 