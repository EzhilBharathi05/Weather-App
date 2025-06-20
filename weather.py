import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = 'e2bfa8d1ec60bc2501cd3d8e3cc7f4ba'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    result_label.config(text="☁️ Fetching weather...", bg="#E0F7FA")

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        weather_data = response.json()

        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        weather_condition = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description'].capitalize()

        weather_result = (
            f"☁️ City: {city}\n"
            f"🌤 Condition: {weather_condition} ({description})\n"
            f"🌡 Temperature: {temperature}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"💨 Wind Speed: {wind_speed} m/s"
        )

        result_label.config(text=weather_result, bg="#E0F7FA")

    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", f"City '{city}' not found!")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Network Error: {e}")

# GUI Setup
root = tk.Tk()
root.title("🌤 Weather App")
root.geometry("450x400")
root.configure(bg="#B3E5FC")  # Sky blue background
root.resizable(False, False)

# Heading
heading_label = tk.Label(
    root,
    text="☀️ Weather App ☁️",
    font=("Arial", 20, "bold"),
    bg="#B3E5FC",
    fg="#01579B"
)
heading_label.pack(pady=15)

# City Entry
city_entry = tk.Entry(root, font=("Arial", 14), width=25, justify='center')
city_entry.pack(pady=10)
city_entry.focus()

# Get Weather Button
get_weather_button = tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 14),
    bg="#0288D1",
    fg="white",
    relief="flat",
    padx=10,
    pady=5,
    command=get_weather
)
get_weather_button.pack(pady=10)

# Cloud Label (just for design)
cloud_label = tk.Label(root, text="☁️☁️☁️", font=("Arial", 18), bg="#B3E5FC")
cloud_label.pack(pady=5)

# Result Display Frame
result_frame = tk.Frame(root, bg="#E0F7FA", bd=2, relief="groove")
result_frame.pack(pady=20, padx=20, fill='both', expand=True)

result_label = tk.Label(
    result_frame,
    text="Enter a city to get started!",
    font=("Arial", 14),
    bg="#E0F7FA",
    justify="left"
)
result_label.pack(padx=10, pady=10)

# Bind Enter key
root.bind("<Return>", lambda event: get_weather())

# Run the App
root.mainloop()
