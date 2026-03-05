import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open('tips_model.pkl','rb'))

st.title("💰 Tip Prediction App")

st.write("Enter restaurant details to predict the tip amount.")

# Inputs
total_bill = st.number_input("Total Bill ($)", min_value=0.0)
size = st.number_input("Number of People", min_value=1)

sex = st.selectbox("Sex", ['Male','Female'])
smoker = st.selectbox("Smoker", ['Yes','No'])
day = st.selectbox("Day", ['Thur','Fri','Sat','Sun'])
time = st.selectbox("Time", ['Lunch','Dinner'])

# Encoding categorical values
sex = 1 if sex == "Male" else 0
smoker = 1 if smoker == "Yes" else 0
time = 1 if time == "Dinner" else 0

day_map = {'Thur':0,'Fri':1,'Sat':2,'Sun':3}
day = day_map[day]

# Create dataframe
input_data = pd.DataFrame({
    'total_bill':[total_bill],
    'size':[size],
    'sex':[sex],
    'smoker':[smoker],
    'day':[day],
    'time':[time]
})

# Prediction
if st.button("Predict Tip"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Tip: ${prediction[0]:.2f}")