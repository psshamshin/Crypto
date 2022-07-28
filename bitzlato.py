from decimal import Decimal
import requests

params = {"asks_limit": "1", "bids_limit": "1"}
API_LINK = "https://bitzlato.bz/api/v2/peatio/"
PAIRS_LIST = [
  "eth_btc",
  "eth_usdt",
  "btc_usdt",
  "bzb_usdt",
  "avax_usdt",
  "btc_mcrerc20",
  "daierc20_usdt"
]
print("\n===== EXCHANGE DATA =====")

for i in PAIRS_LIST: 
  response = requests.get(API_LINK + "public/markets/" + i + "/order-book", params = params).json()
  for j in response["asks"]: print(f"{i} | price: {j['price']} | volume: {j['remaining_volume']}")

print("\n===== P2P DATA =====")
API_LINK_P2P = "https://bitzlato.bz/api/p2p/"
AMOUNT_RUB = int(input("amount RUB: "))
PAYMETHODS = [
  "3547", "443",
  "452", "336",
  "441", "446",
  "1165", "8802"
]
COINS = [
  "BTC", "ETH",
  "BCH", "LTC",
  "DASH", "DOGE",
  "USDT", "USDC",
  "DAI", "MCR",
  "MDT"
]
for coin in COINS:
  print(f"\n----- {coin}/RUB ----")
  for paymethod in PAYMETHODS:
    params = {
      "amount": AMOUNT_RUB, 
      "amountType": "currency%20%2F%20cryptocurrency", 
      "cryptocurrency": coin, 
      "currency": "RUB", 
      "isOwnerActive": "false", 
      "isOwnerVerificated": "false",
      "limit": "1",
      "paymethod": paymethod,
      "skip": "0",
      "type": "purchase"
    }
    
    response = requests.get(API_LINK_P2P + "public/exchange/dsa/", params = params).json()
    if response["total"] != 0:
      owner_name = response["data"][0]["owner"]
      paymethod = response["data"][0]["paymethod"]["name"]
      rate = response["data"][0]["rate"]
      print (f"owner: {owner_name} | rate: {rate} | crypto volume: {round(AMOUNT_RUB / Decimal(rate), 4)} - {paymethod}")