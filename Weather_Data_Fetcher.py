import requests

def fetch_weather(city_name, api_key):
    """
    Fetches weather information for a given city using the Weatherstack API.
    
    :param city_name: Name of the city to fetch weather for.
    :param api_key: Your Weatherstack API key.
    :return: Weather data as a dictionary.
    """
    base_url = "http://api.weatherstack.com/current"
    
    # Parameters including city name and API key
    params = {
        "access_key": api_key,
        "query": city_name,
        "units": "m",  # Temperature in Celsius, wind speed in meters per second
    }

    try:
        # Sends the GET request to Weatherstack API
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises an error for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def display_weather(data):
    """
    Displays weather information from the fetched data.
    
    :param data: Weather data as a dictionary.
    """
    if data and "current" in data:
        # Extracting specific weather details
        city = data.get("location", {}).get("name")
        temperature = data["current"]["temperature"]
        weather_desc = data["current"]["weather_descriptions"][0]
        humidity = data["current"]["humidity"]
        wind_speed = data["current"]["wind_speed"]

        # Displaying the weather information
        print(f"Weather in {city}:")
        print(f"  Temperature: {temperature}°C")
        print(f"  Description: {weather_desc}")
        print(f"  Humidity: {humidity}%")
        print(f"  Wind Speed: {wind_speed} km/h")
    else:
        print("Could not retrieve weather data.")

if __name__ == "__main__":
    # API key from the weatherstack web app
    API_KEY = "a4a63f386b4c27b947bdefabc6422923";
    city = input("Enter the city name: ")
    
    # Fetches weather data and display it
    weather_data = fetch_weather(city, API_KEY)
    display_weather(weather_data)
