import requests
from time import sleep
apiLink = "https://api.coindesk.com/v1/bpi/currentprice.json"

while True:
  sleep(1)
  bitcoinData = requests.get(apiLink)
  price = bitcoinData.json()["bpi"]["USD"]["rate"]
  print("Bitcoin Price: ",price,"USD")
