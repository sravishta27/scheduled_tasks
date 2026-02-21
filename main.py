import requests
import os
from twilio.rest import Client
api_id=os.environ.get("OWM_API_KEY")
endpoint="https://api.openweathermap.org/data/2.5/forecast"
account_sid=os.environ.get("ACCOUNT_SID")
auth_token=os.environ.get("AUTH_TOKEN")
weather_params={
    "lat":17.495922,
    "lon":78.362968,
    "appid": api_id,
    "cnt":4
}
response=requests.get(endpoint, params=weather_params)
response.raise_for_status()
weather_data=response.json()
rain=False
for hour_data in weather_data["list"]:
    condition_code=(hour_data["weather"][0]["id"])
    if int(condition_code)<700:
        rain=True
if rain:
    client=Client(account_sid, auth_token)
    message=client.messages.create(
        body="It's about to rain,carry an umbrella!",
        from_='+18572559551',
        to='+918639017063'
   )
    print(message.status)
