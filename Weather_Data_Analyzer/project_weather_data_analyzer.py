import requests

response = requests.get("https://wttr.in/Lucknow?format=j1")

data = response.json()

current_condition = data["current_condition"][0]

print(current_condition.keys())
print("\n")

temp = current_condition["temp_C"]
humidity = current_condition["humidity"]
pressure = current_condition["pressure"]
wind = current_condition["windspeedKmph"]
feels_like = current_condition["FeelsLikeC"]
description = current_condition["weatherDesc"][0]["value"]

print(f"Temperature_C: {temp}")
print(f"Humidity: {humidity}")
print(f"Pressure: {pressure}")
print(f"Wind_Kmph: {wind}")
print(f"Feels_like_C: {feels_like}")
print(f"Description: {description}")


import pandas as pd

df =pd.DataFrame({
    "Temperature_C": [temp],
    "Feels_Like_C": [feels_like],
    "Humidity": [humidity],
    "Pressure": [pressure],
    "Wind_Speed_Kmph": [wind],
    "Description": [description]
})

print(df)

df.to_csv("weather_data.csv", index = False)

print("Weather data saved successfully!")

print("\n Weather Summary:")

if int(temp) > 32:
    print("It is a hot day.")
elif int(temp) > 25:
    print("Warm Weather.")
else:
    print("Cool Weather.")

if int(humidity) > 70:
    print("High Humidity.")
else:
    print("Normal Humidity.")