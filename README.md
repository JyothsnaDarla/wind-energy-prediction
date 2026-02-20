#  Wind Turbine Energy Prediction Based on Weather Conditions

##  Live Application

🚀 Live Server Link:  
👉 https://wind-energy-prediction-j78f.onrender.com/

Demo:-
https://drive.google.com/file/d/1LnABAHGvCPW6bHKQNRZgh2POOIMsVd0j/view?usp=drive_link

---

## 📌 Project Overview

Wind energy plays a crucial role in renewable energy generation. However, predicting wind turbine power output is challenging due to its dependency on varying weather conditions.

This project is a Machine Learning-powered web application that predicts Wind Turbine Active Power using:

- Wind Speed (m/s)
- Theoretical Power Curve (kWh)

The system integrates real-time weather data with a trained Random Forest regression model and provides predictions through an interactive web interface.

This project demonstrates end-to-end Machine Learning deployment using Flask and cloud hosting.

---

## 🎯 Problem Statement

Wind turbine energy production depends heavily on environmental conditions. Accurate prediction of active power output helps in:

- Energy planning
- Grid management
- Performance monitoring
- Renewable energy optimization

The goal of this project is to build and deploy a predictive model that estimates wind turbine active power based on key parameters.

---

## 🧠 Machine Learning Model

- Algorithm Used: Random Forest Regressor
- Model Type: Supervised Regression
- Input Features:
  - Wind Speed (m/s)
  - Theoretical Power Curve (kWh)
- Output:
  - Predicted Wind Turbine Active Power (kW)

The model was trained on wind turbine operational data and saved as a `.pkl` file for deployment.

---

## 🌍 Real-Time Weather Integration

The application integrates Weather API to:

1. Fetch real-time weather data based on user-entered city.
2. Extract wind speed.
3. Display environmental conditions.
4. Use wind speed for energy prediction.

This creates a real-world simulation of wind energy forecasting.

---

## 🚀 Application Workflow

1️⃣ User enters city name  
2️⃣ Weather API fetches current weather conditions  
3️⃣ Wind speed is extracted and displayed  
4️⃣ User enters theoretical power curve value  
5️⃣ ML model predicts active wind turbine power  
6️⃣ Predicted energy output is displayed instantly  

---

## 🖥 System Architecture

User Interface (HTML/CSS)  
⬇  
Flask Backend (Python)  
⬇  
Weather API Integration  
⬇  
Random Forest ML Model  
⬇  
Prediction Output  

---

## 🛠 Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- HTML
- CSS
- Weather API
- Gunicorn
- Render (Cloud Deployment)

---

## 📂 Project Structure
WindProject/
│
├── app.py
├── wind_active_power_model.pkl
├── requirements.txt
├── Procfile
├── templates/
│ ├── index.html
│ └── windpage.html
├── static/
│ └── style.css
└── README.md

## 👩‍💻 Developed By

Jyothsna Darla  
Final Year B.Tech Student  
Aspiring Machine Learning Engineer | Python Developer  
