import requests

url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=601201&date=03-05-2021"
header={"X-API-KEY" : 'qwertyuiop'}

response =requests.get(url)

print(response.content)