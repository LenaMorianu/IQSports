import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(page_title="IQ_Sports",
                   #page_icon="🧊",
                   layout="wide",
                   initial_sidebar_state="expanded")
         
st.write('Title - Try this IQ TEST')

col1, col2, col3, col4 = st.columns(4)

with col1:
  image = Image.open('Baloncesto1.jpeg')
  st.image(image, caption='Baloncesto')

with col2:
  image2 = Image.open('Tennis1.jpeg')
  st.image(image2, caption='Tennis')

with col3:
  image3 = Image.open('Padel1.jpeg')
  st.image(image3, caption='Padel')

with col4:
  image4 = Image.open('Carrera1.jpeg')
  st.image(image4, caption='Carrera')

st.title('IQ TEST - SPORTS')
         
st.write('')
st.write('*******************************************')

tab1, tab2 = st.tabs(["Preguntas generales", "Preguntas específicas"])
tab1.subheader("Preguntas generales")
#tab1.line_chart(data)

#col1, col2 = st.columns(2)
#with col1:
tab1.write('Select gender:')
tab1.checkbox("Disable text input widget", key="disabled")
tab1.radio(
        "Select age group 👇",
        key="visibility1",
        options=["20 - 29", "30 - 39", "40 - 49","50 - 59", "60 - 69", "70 - 79", "80 - 89", "> 90"],
    )
tab1.radio(
        "Select option 👇",
        key="visibility2",
        options=["Smoker", "Not-smoker"],
    )
tab1.text_input(
        "Estimated number of hours practicing sport by month",
        "This is a placeholder",
        key="placeholder",
    )

#with col2:
tab1.write('Title - Try this IQ TEST')
tab1.text_input(
        "¿Quien ganó el torneo de tenis Roland Garros en 2022? 👇",
        #label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )
    #if text_input:
    #   st.write("You entered: ", text_input)
    
tab2.subheader("Preguntas deporte")
#placeholder = tab2.empty()
#tab2.button = placeholder.button('CALCULAR IQ DEPORTE', disable = False, key = 1)

disabled=tab2.session_state.get("disabled", True)
tab2.boton_calcular_IQ = tab2.button('CALCULAR IQ DEPORTE', on_click=disabled)

if tab2.boton_calcular_IQ:
  IQ = np.random.randint(45, 155)
  tab2.write("IQ: ")
  tab2.write(IQ)
  tab2.write()
  tab2.balloons()
  #tab2.boton_calcular_IQ = tab2.button(disable = True, key = 1)
  #placeholder.button('CALCULAR IQ DEPORTE', disabled=True, key='2')
  #tab2.write(data)
