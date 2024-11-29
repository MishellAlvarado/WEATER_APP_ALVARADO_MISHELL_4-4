from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cv")
def cv():
    return render_template("cv.html")

def get_weather_data(city):
    API_KEY = "f8a5d3e99caa3fdda13dbde6000c9b34"
    idioma = "es"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang={idioma}&appid={API_KEY}"
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

@app.route("/weather", methods=["GET", "POST"])
def weather():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        weather_data = get_weather_data(city)

    return render_template("index.html", weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)

