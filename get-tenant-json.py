import requests
import json

requests.packages.urllib3.disable_warnings()
encoded_body = json.dumps({
                "aaaUser": {
                    "attributes": {
                        "name": "admin",
                        "pwd": "ciscopsdt"
}
}
})
resp = requests.post("https://sandboxapicdc.cisco.com/api/aaaLogin.json", data=encoded_body, verify=False)
header = {"Cookie": "APIC-cookie=" + resp.cookies["APIC-cookie"]}
tenants = requests.get("https://sandboxapicdc.cisco.com/api/node/class/fvTenant.json?rsp-subtree-include=health,faults", headers=header, verify=False)
# print(tenants.text)
json_response = json.loads(tenants.text)
print(json.dumps(json_response, sort_keys=True, indent=4))
