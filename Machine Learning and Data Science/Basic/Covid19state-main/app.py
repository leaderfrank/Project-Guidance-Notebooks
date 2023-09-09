import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Title and Description
st.title('Covid-19 Cases Prediction App')
st.write("Predict the number of Covid-19 cases using a Random Forest Regressor.")

# Input Date
predict_date = st.date_input('Select a date for prediction')
predict_date_ordinal = pd.to_datetime(predict_date).toordinal()

# Load and Prepare Data
df = pd.read_csv('state_wise_daily.csv')
df = df[df.Status == 'Confirmed']
df = df[['Date_YMD', 'TT']].rename(columns={'TT': 'Confirmed'})
df['Date_YMD'] = pd.to_datetime(df['Date_YMD']).map(datetime.toordinal)

# Train-Test Split
X = df['Date_YMD'].values.reshape(-1, 1)
y = df['Confirmed'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the Model
model = RandomForestRegressor(random_state=0)
model.fit(X_train, y_train)

# Predictions
predicted_cases = model.predict([[predict_date_ordinal]])[0].astype(int)
rmse = mean_squared_error(y_test, model.predict(X_test), squared=False)
score = model.score(X, y) * 100

# Display Results
st.write(f"Predicted cases for {predict_date}: **{predicted_cases}**")
st.write(f"Model RMSE: **{rmse:.2f}**")
st.write(f"Model Accuracy: **{score:.2f}%**")

# Plot
st.line_chart(df.set_index('Date_YMD')['Confirmed'])

# Footer
st.write("Made by Suyash Singh using Random Forest Regression")
