# Import the requests library
import requests

# NASA POWER API URL
url = "https://power.larc.nasa.gov/api/temporal/hourly/point"

# Parameters for the API request
params = {
    "community": "SB",             # Sustainable Buildings community
    "parameters": "T2M",           # Temperature at 2 Meters
    "latitude": 37.1,
    "longitude": -76.39,
    "start": "20240101",
    "end": "20241231",
    "format": "JSON"
}

# Send the request to NASA's server
response = requests.get(url, params=params)

# Convert the response into JSON format
data = response.json()

# Print the first few temperature values
temperature = data["properties"]["parameter"]["T2M"]

print("First 10 observations:\n")

for i, (timestamp, value) in enumerate(temperature.items()):
    print(timestamp, ":", value, "C")
    
    if i == 9:
        break
