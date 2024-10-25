import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import time
import sys

ap = "ur apikey"
base_url = "http://api.weatherapi.com/v1/current.json"
console = Console()

def get_weather(city_name):
    params = {
        "key": ap,
        "q": city_name,
        "aqi": "no"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

def loading_animation(duration=3):
    end_time = time.time() + duration
    while time.time() < end_time:
        for symbol in ["|", "/", "-", "\\"]:
            sys.stdout.write(f"\rloading {symbol}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r" + " " * 30 + "\r")
def display_weather(data, city_name):
    location = data["location"]
    current = data["current"]
    table = Table(title=f"weather in {location['name']}, {location['country']}", style="bold magenta")
    table.add_column("attribute", style="cyan", no_wrap=True)
    table.add_column("value", style="green")
    table.add_row("temperature", f"{current['temp_c']}°C")
    table.add_row("feels like", f"{current['feelslike_c']}°C")
    table.add_row("humidity", f"{current['humidity']}%")
    table.add_row("wind speed", f"{current['wind_kph']} km/h")
    table.add_row("description", current["condition"]["text"])
    console.print(table)

def main():
    console.print(Panel("follow me on github now!!! (type [bold cyan]exit[/bold cyan] to quit)", style="bold magenta"))
    while True:
        city_name = console.input("\n[bold magenta]enter a city:[/bold magenta] ")
        if city_name.lower() == "exit":
            console.print("[bold black]bye nigga[/bold black]")
            break
        loading_animation()
        data = get_weather(city_name)
        if data:
            display_weather(data, city_name)
        else:
            console.print(f"[bold red]huh?[/bold red] '{city_name}' is not a valid city")

if __name__ == "__main__":
    main()
