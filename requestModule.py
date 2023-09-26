import requests as req
import json

resp=req.get("https://jsonplaceholder.typicode.com/users")
# resp=req.get("https://www.w3schools.com/python/demopage.htm")
result=json.loads(resp.text)
# print(type(result))
for user in result:
    print(f"{user['name']},{user['phone']},{user['address']['city']}")

# op=filter(lambda user:user['address']['city']=='Howemouth',result)
# print(list(op))

