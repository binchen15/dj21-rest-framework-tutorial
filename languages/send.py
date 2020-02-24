import requests

token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgyNDI2MjM2LCJqdGkiOiIxYmExNjA3OThmMWM0NmI2Yjg3MjliYWEwMTYxYmY5ZSIsInVzZXJfaWQiOjF9.2uoG8TpoQu2rouBWjyvMXfTb4oybRv_kqfMqFMR5Mp4'

headers = {}
headers['Authorization'] = 'Bearer ' + token

r = requests.get("http://localhost:8000/api/paradigms", headers=headers)
print(r.text)

