# Weather Data Fetcher Using Weatherstack API

This Python program fetches and displays **real-time weather information** for any city using the **Weatherstack API**. The app provides the current temperature, weather description, humidity, and wind speed for the specified city in a simple and user-friendly graphical interface.

---

## Features:
1. **Fetches real-time weather data** for a given city.
2. Displays key weather information:
    - **Temperature** (°C)
    - **Weather description** (e.g., sunny, rainy)
    - **Humidity** (%)
    - **Wind speed** (km/h)
3. Simple **GUI-based interface** using **Tkinter**.
4. **Error handling** with helpful messages if the API call fails or if the city name is invalid.

---

## Prerequisites

Before running this script, ensure you have:
1. **Python 3.x** installed.
2. **`requests`** and **`tkinter`** libraries installed. 
    - If not, install the `requests` library using:
      ```bash
      pip install requests
      ```
    - `tkinter` is included by default in Python 3.x, but you may need to install it separately depending on your environment.
3. A valid **Weatherstack API key**. 
    - Sign up for a free or paid account at Weatherstack and obtain your API key.

---

## How It Works

1. The script uses the **Weatherstack API** to fetch current weather data for a specified city.
2. It sends a GET request to Weatherstack with the **city name** and **API key**.
3. The data is processed and displayed in a **Tkinter GUI** on the screen.
4. The user enters the city name, and the weather information is displayed dynamically.

---

## Usage

### Step 1: Get Your Weatherstack API Key
1. Visit [Weatherstack](https://weatherstack.com/) and sign up for a free account.
2. Obtain your **API Key** from the API keys page.

### Step 2: Set Up Your API Key
1. Download or clone this repository.
2. Open the Python script `weather_fetcher_gui.py`.
3. Replace the placeholder `your_weatherstack_api_key_here` in the script with your actual Weatherstack API key.

### Step 3: Run the Program
1. Navigate to the project folder where `weather_fetcher_gui.py` is saved.
2. Run the script:
    ```bash
    python weather_fetcher_gui.py
    ```
3. Enter the city name when prompted in the GUI to fetch the weather information.

---

## Error Handling

- If the script cannot fetch data due to network issues or invalid city names, it will display an error message using Tkinter messageboxes.
- If the **city name** is empty or invalid, the app will prompt the user to provide a valid input.
- If there's an issue with the **API key** or if the request to the Weatherstack API fails, an error message will be shown in the GUI.

---

## Future Improvements
- **Support for multiple cities** at once: Ability to fetch and display weather data for multiple cities simultaneously.
- **Error handling for invalid API keys**: Provide more detailed feedback if the API key is incorrect or if there is an issue with the API response.
- **Weather forecast**: Extend the app to fetch a weather forecast for the next few days in addition to the current weather.
- **Graphical data presentation**: Display weather data using **charts** or **graphs** (e.g., temperature trends over time).

---
