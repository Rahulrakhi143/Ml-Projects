# electricity_predictor.py
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Step 1: Create simple dataset
data = []
for _ in range(100):
    appliances = np.random.randint(1, 10)
    hours = np.random.uniform(1, 8)
    days = np.random.randint(25, 32)
    power = np.random.randint(100, 2000)  # watts
    rate = np.random.uniform(4, 8)  # ₹ per kWh

    kwh = (appliances * power * hours * days) / 1000
    cost = kwh * rate
    data.append([appliances, hours, days, power, rate, kwh, cost])

df = pd.DataFrame(data, columns=["appliances", "hours", "days", "power", "rate", "kwh", "cost"])

# Step 2: Train model
X = df[["appliances", "hours", "days", "power", "rate"]]
y = df[["kwh", "cost"]]

model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "electricity_model.pkl")
print("✅ Model trained and saved.")



# predict.py
import joblib

# Load model
model = joblib.load("electricity_model.pkl")

# Get user input
a = int(input("Appliances: "))
h = float(input("Hours/day: "))
d = int(input("Days: "))
p = int(input("Power (W): "))
r = float(input("Rate (₹/kWh): "))

# Predict
x = [[a, h, d, p, r]]
kwh, cost = model.predict(x)[0]

# Show result
print(f"\n⚡ Estimated usage: {kwh:.2f} kWh")
print(f"💰 Estimated bill: ₹{cost:.2f}")
