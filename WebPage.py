import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from PIL import Image
#import altair as alt
#from googleapiclient.discovery import build
#from google.oauth2 import service_account
#from google.oauth2 import service_account
#from gsheetsdb import connect # Create a connection object.


st.set_page_config(page_title="IQ_Sports",
                   layout="wide",
                   initial_sidebar_state = "expanded")

st.markdown("<h1 style='text-align: center; color: blue;'> IQ SPORTS TEST </h1>", unsafe_allow_html=True)
st.write('')
st.write('')


with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")

# Create a connection object.

#scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
#        "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

#creds = None
#creds = service_account.Credentials.from_service_account_info( st.secrets["gcp_service_account"], scopes="https://www.googleapis.com/auth/spreadsheets" )
#conn = connect(credentials=creds)


# The ID spreadsheet.
#SAMPLE_SPREADSHEET_ID=st.secrets["SAMPLE_SPREADSHEET_ID"]["SAMPLE_SPREADSHEET_ID"]
#service = build('sheets','v4',credentials=creds)



#@st.cache_data(ttl=600)
#def run_query(query):
#    rows = conn.execute(query, headers=1)
#    rows = rows.fetchall()
#    return rows

#sheet_url = st.secrets["public_gsheets_url"]
#rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
#for row in rows:
#    st.write(row)



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

#url0 = 'https://github.com/LenaMorianu/IQSports/blob/56bafa1b74865608024adf061bd7223059a4dea4/Data.csv'
#url1 = 'https://raw.githubusercontent.com/LenaMorianu/IQSports/main/Data.csv'

#@st.cache
#def load_data(url):
#  data = pd.read_csv(url, encoding='ISO-8859-1')
  #data.drop(['Unnamed: 0'], axis=1, inplace=True)
#  return data

#df = load_data(url1)
#st.write(df)

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
 

#columnas = ["Nombre", "Edad", "Deporte_favorito", "Horas_deporte", "Pregunta1", "Pregunta2", "Pregunta3", "IQ"]
#data1 = [[Nombre, Edad, Deporte_favorito, Horas_deporte, Respuesta1, Respuesta2, Respuesta3, IQ]]
#df2 = pd.DataFrame(data1, columns = columnas)
#st.write(df2)

#df3 = st.df.append([[Nombre], [Edad], [Deporte_favorito], [Horas_deporte], [Respuesta1], [Respuesta2], [Respuesta3]])
#tab2.write(df3)
#df2.to_csv('https://raw.githubusercontent.com/LenaMorianu/IQSports/main/Data.csv', mode='w', index=False, header=False, sep=';', encoding='ISO-8859-1')


def write_csv_func(data1, data2, data3, data4, data5, data6, data7):    
    with open('Data.csv', 'a+') as f:    #Append & read mode
        f.write(f"{data1},{data2}, {data3}, {data4}, {data5}, {data6}, {data7}\n")
        st.write("DONE")
 
@st.cache
def convert_df(df):
  return df.to_csv(mode='a', header = ["Nombre", "Edad", "Deporte_favorito", "Horas_deporte", "Pregunta1", "Pregunta2", "Pregunta3", "IQ"]).encode('utf-8')
  

@st.cache_data()
def load_data2(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)


#sh = gc.open_by_key('1FRXkZmD0hbzxmRONVrY3fkzKMC4FzdYix8t6bfFXugU')
#worksheet = sh.sheet1
#dataframe = pd.DataFrame(worksheet.get_all_records())
#worksheet.update([dataframe.columns.values.tolist()] + dataframe.values.tolist())
#worksheet.update(dataframe.values.tolist([[1],[2],[3],[4],[5],[6],[7]))
  
#st.write(dataframe) 


boton_calcular_IQ = tab2.button('CALCULAR IQ DEPORTE', key='iq_button')
tab2.write()
 
if 'IQ' not in st.session_state:
    st.session_state.IQ =  np.random.randint(45, 155)


    
if boton_calcular_IQ:
  IQ = st.session_state.IQ
  #tab2.metric(label="IQ", value=IQ)
  #write_csv_func(Nombre, Edad, Deporte_favorito, Horas_deporte, Respuesta1, Respuesta2, Respuesta3)
  tab2.write('IQ:')
  #tab2.markdown("<h1 style='text-align: center; color: blue;'> IQ </h1>", unsafe_allow_html=True)
  tab2.write()
  tab2.write(IQ)
  tab2.balloons()
  columnas = ["Nombre", "Edad", "Deporte favorito", "Horas deporte", "Pregunta1", "Pregunta2", "Pregunta3", "IQ"]
  data1 = [[Nombre, Edad, Deporte_favorito, Horas_deporte, Respuesta1, Respuesta2, Respuesta3, IQ]]
  df2 = pd.DataFrame(data1, columns = columnas)
  st.write(df2)
  csv_file = convert_df(df2)
  st.download_button(
    label="Download data as CSV",
    data=csv_file,
    file_name='Datos.csv',
    mime='text/csv',
  )
  
#arr = np.random.normal(1, 1, size=100)
#fig, ax = plt.subplots()
#ax.hist(arr, bins=30)

#st.pyplot(fig)
  
