import pandas as pd

import streamlit as st 

st.title("Streamlit Example")
st.write("This is an example of using Streamlit to create a simple web app.")
st.write("You can use Streamlit to create interactive web apps with Python.")

df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': [5, 6, 7, 8]
})  
st.write("Here is a simple DataFrame:")
st.dataframe(df)
st.write("You can also create interactive widgets. For example, here is a slider:")
slider_value = st.slider("Select a value", 0, 100) # Default value is 50 and range is from 0 to 100
st.write(f"You selected: {slider_value}")
st.write("You can also create a button:")
if st.button("Click me"):
    st.write("Button clicked!")
st.write("This is just a simple example. Streamlit has many more features that you can explore!")


uploaded_file =  st.file_uploader("Choose a file" , type=["csv", "xlsx"])
if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    st.write("Here is the uploaded file:")
    st.dataframe(df)
