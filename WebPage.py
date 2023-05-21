import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(page_title="IQ_Sports",
                   #page_icon="🧊",
                   layout="wide",
                   initial_sidebar_state="expanded")

st.markdown("<h1 style='text-align: center; color: blue;'> IQ SPORTS TEST </h1>", unsafe_allow_html=True)
st.write('')
st.write('')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
  image = Image.open('Baloncesto1.jpeg')
  st.image(image, caption='Baloncesto', width=200)

with col2:
  image2 = Image.open('Tennis1.jpeg')
  st.image(image2, caption='Tennis', width=200)

with col3:
  image3 = Image.open('Padel1.jpeg')
  st.image(image3, caption='Padel', width=200)
  
with col4:
  image4 = Image.open('Carrera1.jpeg')
  st.image(image4, caption='Carrera', width=200)
  
with col5:
  image5 = Image.open('Balonmano1.jpeg')
  st.image(image5, caption='Balonmano', width=200)

st.write('')
#st.write('*******************************************')
#st.write('')

tab1, tab2 = st.tabs(["Preguntas generales", "Preguntas específicas"])

tab1.subheader("Preguntas generales")
st.write('')

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    
#col1, col2 = st.columns(2)
#with col1:
#tab1.write(:')
#tab1.checkbox("Disable text input widget", key="disabled")

Nombre=tab1.text_input(
  "Nombre: 👇",
  #label_visibility=st.session_state.visibility,
  #disabled=tab1.session_state.disabled,
  #placeholder=tab1.session_state.placeholder,
)
  
tab1.write(Nombre)
tab1.write('')
tab1.radio(
  "Edad 👇",
  key="visibility1",
  options=["20 - 29", "30 - 39", "40 - 49","50 - 59", "60 - 69", "70 - 79", "80 - 89", "> 90"],)

tab1.radio(
  "Select option 👇",
  key="visibility2",
  options=["Smoker", "Not-smoker"],)

tab1.text_input(
    "Estimated number of hours practicing sport by month",
    "This is a placeholder",
    key="placeholder",)

#with col2:

tab2.subheader("Preguntas deporte")
Respuesta1 = tab2.text_input(
    "¿Quien ganó el torneo de tenis Roland Garros en 2022? 👇",
    #label_visibility=st.session_state.visibility,
    #disabled=st.session_state.disabled,
    #placeholder=st.session_state.placeholder,
)

if Respuesta1:
  st.write("You entered: ", Respuesta1)
 
def disable():
    st.session_state.disabled = True
    
tab2.boton_calcular_IQ = tab2.button('CALCULAR IQ DEPORTE', key='iq_button', on_click=disable)
tab2.write()

if "iq_button" in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = True
    
if tab2.boton_calcular_IQ:
  IQ = np.random.randint(45, 155)
  tab2.metric(label="IQ", value=IQ)
  tab2.write()
  tab2.write()
  tab2.balloons()
  #tab2.session_state.disabled = True
  #tab2.button(key='iq_button', disabled=True)
  
st.write(st.session_state.key)

