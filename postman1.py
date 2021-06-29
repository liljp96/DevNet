import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer Y2E2M2E1OGQtNTc5MC00NmQ5LWJjYjUtNGI0MTBiNDhkNjFiYzFiYzM3M2EtMGE0_PF84_consumer',
  'Cookie': '__cfduid=d089567e4d6cf5f5a51181a0252e2ae121600460018'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

deck = response.json()
deck_id = deck['deck_id']
print(deck_id)
