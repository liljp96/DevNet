import requests

url = "https://devnetapi.cisco.com/sandbox/apic_em/api/v1/ticket"

payload = "{\n    \"username\": \"devnetuser\",\n    \"password\": \"Cisco123!\"\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))