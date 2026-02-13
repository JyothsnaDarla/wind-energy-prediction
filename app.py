from flask import Flask, render_template, request
import pickle
import pandas as pd
import requests

app = Flask(__name__)

# Load trained Random Forest model
model = pickle.load(open("wind_active_power_model.pkl", "rb"))

# ------------------ HOME PAGE ------------------
@app.route('/')
def home():
    return render_template("index.html")


# ------------------ WEATHER PAGE ------------------
@app.route('/windpage')
def windpage():
    return render_template("windpage.html")


# ------------------ WEATHER API ------------------
@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']

    API_KEY = "91e09a1b1f9542e687990234261202"
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    response = requests.get(url)
    data = response.json()

    temperature = data['current']['temp_c']
    humidity = data['current']['humidity']
    pressure = data['current']['pressure_mb']
    wind_speed = data['current']['wind_kph'] / 3.6  # convert to m/s

    return render_template("windpage.html",
                           temperature=temperature,
                           humidity=humidity,
                           pressure=pressure,
                           wind_speed=round(wind_speed,2),
                           city=city)


# ------------------ PREDICTION ------------------
@app.route('/predict', methods=['POST'])
def predict():
    wind_speed = float(request.form['wind_speed'])
    theoretical_power = float(request.form['theoretical_power'])

    input_df = pd.DataFrame({
        'Wind Speed (m/s)': [wind_speed],
        'Theoretical Power Curve (kWh)': [theoretical_power]
    })

    prediction = model.predict(input_df)

    return render_template("windpage.html",
                           prediction=round(prediction[0],2))


import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

