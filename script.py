import requests

# Git Test 123

r = requests.get("https://coreyms.com")
print(r.status_code)
print(r.ok)
