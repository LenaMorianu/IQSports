import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(page_title="IQ_Sports",
                   #page_icon="🧊",
                   layout="wide",
                   initial_sidebar_state = "expanded")

st.markdown("<h1 style='text-align: center; color: blue;'> IQ SPORTS TEST </h1>", unsafe_allow_html=True)
st.write('')
st.write('')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
  image = Image.open('Photos/Baloncesto1.jpeg')
  st.image(image, caption='Baloncesto', width=200)

with col2:
  image2 = Image.open('Photos/Tennis1.jpeg')
  st.image(image2, caption='Tennis', width=200)

with col3:
  image3 = Image.open('Photos/Padel1.jpeg')
  st.image(image3, caption='Padel', width=200)
  
with col4:
  image4 = Image.open('Photos/Carrera1.jpeg')
  st.image(image4, caption='Carrera', width=200)
  
with col5:
  image5 = Image.open('Photos/Balonmano1.jpeg')
  st.image(image5, caption='Balonmano', width=200)

st.write('')
#st.write('*******************************************')
#st.write('')

#url0 = 'https://github.com/LenaMorianu/IQSports/blob/56bafa1b74865608024adf061bd7223059a4dea4/Data.csv'
url1 = 'https://raw.githubusercontent.com/LenaMorianu/IQSports/main/Data.csv'

#@st.cache
def load_data(url):
  data = pd.read_csv(url, encoding='ISO-8859-1')
  #data.drop(['Unnamed: 0'], axis=1, inplace=True)
  return data

df = load_data(url1)
st.write(df)

tab1, tab2 = st.tabs(["Preguntas generales", "Preguntas específicas"])


tab1.subheader("Preguntas generales")
tab1.write('')


tab1.write(" --------- ")
#tab1.checkbox("Disable text input widget", key="disabled")

#Column NOMBRE
Nombre = tab1.text_input(
  "Nombre: 👇",
    #key = nombre,
    #label_visibility=st.session_state.visibility,
    #disabled=tab1.session_state.disabled,
    #placeholder=tab1.session_state.placeholder,
    )

             
#with col2:             
tab1.write(Nombre)
tab1.write('')

#Column EDAD
Edad = tab1.radio(
  "Edad 👇",
  #key="edad",
  options=["20 - 29", "30 - 39", "40 - 49","50 - 59", "60 - 69", "70 - 79", "80 - 89", "> 90"],)

#Column DEPORTE_FAVORITO
Deporte_favorito = tab1.text_input(
  "Deporte favorito: 👇",
    #key = deporte_favorito,
    #label_visibility=st.session_state.visibility,
    #disabled=tab1.session_state.disabled,
    #placeholder=tab1.session_state.placeholder,
  )

#Column HORAS_DEPORTE
Horas_deporte = tab1.radio(
  "Horas de deporte realizadas a la semana: 👇",
  #key= horas_deporte,
  options=["<1", " 1 - 3", " 3 - 5" , "5 - 7", ">7"],
  )


tab2.subheader("Preguntas deporte")
Respuesta1 = tab2.text_input(
    "¿Quien ganó el torneo de tenis Roland Garros en 2022? 👇",
    #label_visibility=st.session_state.visibility,
    #disabled=st.session_state.disabled,
    #placeholder=st.session_state.placeholder,
)

if Respuesta1:
  st.write("Respuesta : ", Respuesta1)   
  
Respuesta2 = tab2.text_input(
    "¿Quien ganó la última Copa del Rey de baloncesto? 👇",
    #label_visibility=st.session_state.visibility,
    #disabled=st.session_state.disabled,
    #placeholder=st.session_state.placeholder,
)

if Respuesta2:
  st.write("Respuesta : ", Respuesta2)   
  

Respuesta3 = tab2.text_input(
    "¿Qué equipo femenino ganó el último Campeonato del Mundo de balonmano? 👇",
    #label_visibility=st.session_state.visibility,
    #disabled=st.session_state.disabled,
    #placeholder=st.session_state.placeholder,
)

if Respuesta3:
  st.write("Respuesta : ", Respuesta3)   
    
columnas = ["Nombre", "Edad", "Deporte_favorito", "Horas_deporte", "Pregunta1", "Pregunta2", "Pregunta3"]

df2 = pd.DataFrame([Nombre, Edad, Deporte_favorito, Horas_deporte, Respuesta1, Respuesta2, Respuesta3] , columns = columnas)

pd.df2.append([Nombre, Edad, Deporte_favorito, Horas_deporte, Respuesta1, Respuesta2, Respuesta3])
tab2.write(df2)
#df2.to_csv('https://raw.githubusercontent.com/LenaMorianu/IQSports/main/Data.csv', mode='w', index=False, header=False, sep=';', encoding='ISO-8859-1')


def write_csv_func(data1, data2, data3, data4, data5, data6, data7):    
    with open('Data.csv', 'a+') as f:    #Append & read mode
        f.write(f"{data1},{data2}, {data3}, {data4}, {data5}, {data6}, {data7}\n")
        st.write("DONE")
 
@st.cache
def convert_df(df):
    return df.to_csv(mode='w').encode('utf-8')

csv_file = convert_df(df2)

     
boton_calcular_IQ = tab2.button('CALCULAR IQ DEPORTE', key='iq_button')
tab2.write()
 
if 'IQ' not in st.session_state:
    st.session_state.IQ =  np.random.randint(45, 155)

if boton_calcular_IQ:
  IQ = st.session_state.IQ
  #tab2.metric(label="IQ", value=IQ)
  #write_csv_func(Nombre, Edad, Deporte_favorito, Horas_deporte, Respuesta1, Respuesta2, Respuesta3)
  tab2.write('IQ:')
  tab2.write(IQ)
  tab2.balloons()
  st.download_button(
    label="Download data as CSV",
    data=csv_file,
    file_name='Prueba.csv',
    mime='text/csv',
  )   
    
  #tab2.session_state.disabled = True
  #tab2.button(key='iq_button', disabled=True)

  


