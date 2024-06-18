import requests

url = 'https://westinpay.com/currency/fiat_api?api_key=YOUR-API-KEY&base=USD&output=JSON'
response = requests.get(url)
data = response.json()
print(data)
