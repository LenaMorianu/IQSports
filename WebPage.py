import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="IQ_Sports",
                   #page_icon="🧊",
                   layout="wide",
                   initial_sidebar_state="expanded")

st.title('IQ TEST - SPORTS')
         
st.write('Title - Try this IQ TEST')
  
st.write('')
st.write('*******************************************')

tab1, tab2 = st.tabs(["Preguntas generales", "Preguntas específicas"])
tab1.subheader("Preguntas generales")
#tab1.line_chart(data)

#col1, col2 = st.columns(2)
#with col1:
tab1.st.write('Select gender:')
tab1.st.checkbox("Disable text input widget", key="disabled")
tab1.st.radio(
        "Select age group 👇",
        key="visibility1",
        options=["20 - 29", "30 - 39", "40 - 49","50 - 59", "60 - 69", "70 - 79", "80 - 89", "> 90"],
    )
tab1.st.radio(
        "Select option 👇",
        key="visibility2",
        options=["Smoker", "Not-smoker"],
    )
tab1.st.text_input(
        "Estimated number of hours practicing sport by month",
        "This is a placeholder",
        key="placeholder",
    )

#with col2:
tab1.st.write('Title - Try this IQ TEST')
tab1.st.text_input(
        "¿Quien ganó el torneo de tenis Roland Garros en 2022? 👇",
        #label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )
    #if text_input:
    #   st.write("You entered: ", text_input)
    
tab2.subheader("Preguntas deporte")
data = np.random.randn(1, 155)
tab2.write(data)
