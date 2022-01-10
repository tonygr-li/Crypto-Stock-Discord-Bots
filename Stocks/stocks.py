import requests, time, re, os
import pandas as pd
import pickle as pkl
import openpyxl


def stock_info(name):
  df = pd.read_excel('company_list.xlsx')
  symbols = df['Symbol'].values.tolist()
  if name in symbols:
    url = 'https://api.tdameritrade.com/v1/instruments'
    payload = {
          'apikey': 'test',
          'symbol': name,
          'projection': 'fundamental'
      }
    results = requests.get(url,params=payload)
    price = results.json()
    correct = price.get(name)
    correct1 = correct.get("fundamental")
    final = "" + "\n"


    for x, y in correct1.items():
      final += str(x) + " " + str(y) + "\n"

  else:
    error_message = "Please enter a valid symbol or search it online (make sure it is capitalized)"
    return error_message

  return final

# Stock Price

def stock_price(name):
  df = pd.read_excel('company_list.xlsx')
  symbols = df['Symbol'].values.tolist()
  if name in symbols:
    full_url = "https://api.tdameritrade.com/v1/marketdata/quotes"
    payload = {
          'apikey': 'test',
          'symbol': name

      }
    results = requests.get(full_url,params=payload)
    response = results.json()
    correct = response.get(name)
    stock_name = "Stock name: " + correct.get('symbol')
    stock_description = "Description: " + correct.get('description')
    price = "Last Price: " + str(correct.get('lastPrice'))
    bid_price = "Bid Price: " + str(correct.get('bidPrice'))
    ask_price = "Ask Price: " + str(correct.get('askPrice'))
    open_price = "Open Price: " + str(correct.get('openPrice'))
    close_price = "Close Price: " + str(correct.get('closePrice'))
    high_price = "High Price: " + str(correct.get('highPrice'))
    low_price = "Low Price: " + str(correct.get('lowPrice'))
    final = stock_name + "\n" + stock_description + "\n" + price + "\n" + bid_price + "\n" + ask_price + "\n" + high_price + "\n" + low_price + "\n" + open_price + "\n" + close_price + "\n"

  else:
    error_message = "Please enter a valid symbol"
    return error_message

  return final

  def my_stocks():
    google = stock_price("GOOGL")

    final_text = google + "\n\n"
    return final_text
