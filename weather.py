import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
API_KEY = os.environ.get("API_KEY")

def get_weather(city_name):
    """Feathes weather data for a given city."""

    # This is the URL (API endpointer) we are calling
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    # These are the parameters we send with requests
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() # Raises an error for bad responses (like 404)

        data = response.json() # Converts the text response to a Python dictionary

        # -- Display the weather --
        main_weather = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']

        print(f"\n--- Weather in {city_name} ---")
        print(f"Sky: {main_weather} ({description})")
        print(f"Temperature: {temp}°C")
        print(f"Feels Like: {feels_like}°C")
        print("------------------------")
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            print(f"Error: City '{city_name}' not found.")
        elif response.status_code == 401:
            print("Error: Invalid API key. Check your .env file.")
        else:
            print(f"An HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def main():
    """Main function to run the weather app."""
    while True:
        city = input("Enter a city name (or 'exit' to quit): ")
        if city.lower() == 'exit':
            print("Goodbye!")
            break

        if city:
            get_weather(city)

if __name__ == "__main__":
    main()