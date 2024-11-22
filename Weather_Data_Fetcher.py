import requests
import tkinter as tk
from tkinter import messagebox

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
        # Send the GET request to Weatherstack API
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def display_weather(data):
    """
    Displays weather information in the GUI from the fetched data.
    
    :param data: Weather data as a dictionary.
    """
    if data and "current" in data:
        city = data.get("location", {}).get("name")
        temperature = data["current"]["temperature"]
        weather_desc = data["current"]["weather_descriptions"][0]
        humidity = data["current"]["humidity"]
        wind_speed = data["current"]["wind_speed"]

        # Update the weather info in the GUI
        result_text.set(f"Weather in {city}:\n"
                        f"Temperature: {temperature}°C\n"
                        f"Description: {weather_desc}\n"
                        f"Humidity: {humidity}%\n"
                        f"Wind Speed: {wind_speed} km/h")
    else:
        messagebox.showerror("Error", "Could not retrieve weather data.")

def get_weather():
    """
    Handles the button click to fetch weather data for the city entered.
    """
    city = city_entry.get()
    if city.strip() == "":
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    # Fetch weather data
    weather_data = fetch_weather(city, API_KEY)
    display_weather(weather_data)

# Set up the Tkinter GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# API Key for Weatherstack (you should replace this with your actual API key)
API_KEY = "a4a63f386b4c27b947bdefabc6422923"  # Replace with your actual key

# Title label
title_label = tk.Label(root, text="Weather App", font=("Arial", 24, "bold"), bg="#3b7bbf", fg="white", pady=20)
title_label.pack(fill="both")

# City input field
city_label = tk.Label(root, text="Enter City:", font=("Arial", 14), bg="#f0f0f0")
city_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14), width=30)
city_entry.pack(pady=10)

# Fetch weather button
fetch_button = tk.Button(root, text="Get Weather", font=("Arial", 14), bg="#4CAF50", fg="white", command=get_weather)
fetch_button.pack(pady=20)

# Result display area
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 14), bg="#f0f0f0", anchor="w", justify="left")
result_label.pack(padx=20, pady=10)

# Run the Tkinter event loop
root.mainloop()
