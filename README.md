# Weather Data Fetcher Using Weatherstack API

This Python program fetches and displays real-time weather information for any city using the **Weatherstack API**. It provides the current temperature, weather description, humidity, and wind speed for the specified city.

---

## Features
1. Fetches **real-time weather data** for a given city.
2. Displays key weather information:
   - Temperature (°C)
   - Weather description (e.g., sunny, rainy)
   - Humidity (%)
   - Wind speed (km/h)
3. Simple and easy-to-use command-line interface.

---

## Prerequisites
Before running this script, ensure you have:
1. **Python 3.x** installed.
2. **`requests` library** installed. If not, install it using:
- pip install requests
3. Weatherstack API key. Sign up for a free or paid account at Weatherstack and obtain your API key.

---

### How It Works

1. The script uses the Weatherstack API to fetch current weather data for a specified city.
2. It sends a GET request to Weatherstack with the city name and API key.
3. The data is processed and displayed on the console.

---

### Usage

#### Step 1: Get Your Weatherstack API Key

1. Visit Weatherstack and sign up for a free account.
2. Obtain your API Key from the API keys page.

#### Step 2: Set Up Your API Key

1. Download or clone this repository.
2. Open the Python script weather_fetcher.py.
3. Replace the placeholder "your_weatherstack_api_key_here" in the script with your actual Weatherstack API key.

#### Step 3: Run the Program

1. Navigate to the project folder where weather_fetcher.py is saved.
2. Run the script:
- python weather_fetcher.py
3. Enter the city name when prompted to fetch the weather information.

---

#### Error Handling

- If the script cannot fetch data due to network issues or invalid city names, it will display an error message.
- Ensure you have entered a valid city name and your API key is correct.

---

#### Future Improvements
- Support for multiple cities at once.
- Error handling for invalid API keys or bad responses.
- Extend the script to fetch a weather forecast for the upcoming days.


