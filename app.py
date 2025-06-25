from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            return None
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind": data["wind"]["speed"],
            "description": data["weather"][0]["description"].title()
        }
    except:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        weather = get_weather_data(city)
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)

