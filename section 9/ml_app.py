import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# تحميل البيانات
data = load_iris(as_frame=True)
df = data.data
target = data.target

# تدريب الموديل
model = RandomForestClassifier()
model.fit(df, target)

# UI
st.title("Iris Dataset Prediction 🌸")
st.write("Predict iris species using ML")

# sliders
sepal_length = st.slider(
    "Sepal Length",
    float(df['sepal length (cm)'].min()),
    float(df['sepal length (cm)'].max()),
    float(df['sepal length (cm)'].mean())
)

sepal_width = st.slider(
    "Sepal Width",
    float(df['sepal width (cm)'].min()),
    float(df['sepal width (cm)'].max()),
    float(df['sepal width (cm)'].mean())
)

petal_length = st.slider(
    "Petal Length",
    float(df['petal length (cm)'].min()),
    float(df['petal length (cm)'].max()),
    float(df['petal length (cm)'].mean())
)

petal_width = st.slider(
    "Petal Width",
    float(df['petal width (cm)'].min()),
    float(df['petal width (cm)'].max()),
    float(df['petal width (cm)'].mean())
)

# prediction
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(input_data)

# عرض النتيجة
st.success(f"Predicted species: {data.target_names[prediction][0]} 🌼")