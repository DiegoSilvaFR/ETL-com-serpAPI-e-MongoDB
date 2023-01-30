import requests
import pandas as pd
import time


def trans_str(string):
  """Função que substitue em uma string \n por uma espaço vazio"""
  return string.replace("\n"," ")

def call_API(start,search):
  """Função que irá se conectar a API extrair os dados e torna-los em dados relacionas por meio do acote pandas"""
  API_KEY = "e815363f593f50749db95315360f3f69de555692944a06b24acf8f59ee4b71ad"    #exemplo da Key necessaria para se conectar à API
  lingua = "pt" 
  pais = "br"
  js = requests.get(f"https://serpapi.com/search.json?key={API_KEY}&engine=google_jobs&q={search}&hl={lingua}&gl={pais}&start={start}").json()

  time.sleep(1)
  titulo = []
  empresa = []
  anuncio = []
  desc = []
  for i in range(len(js['jobs_results'])):
     titulo.append(js['jobs_results'][i]["title"])           #titulo.append(tradutor(js['jobs_results'][i]["title"]).text)
     empresa.append(js['jobs_results'][i]['company_name'])
     anuncio.append(js['jobs_results'][i]["via"].replace("via ",""))
     desc.append(js['jobs_results'][i]["description"].replace("\n"," "))     #desc.append(transform(js['jobs_results'][i]["description"].replace("\n"," ")))
  return titulo,empresa,anuncio,desc

consultas = ["Cientista de Dados", "Data Scientist"]
df = pd.DataFrame(columns = ["title","company","announcement","description"])

for consulta in consultas:
  cont = 0
  while True:
    try:
      titulo,empresa,anuncio,desc = call_API(cont,consulta)
      df = pd.concat([df,pd.DataFrame({"title":titulo,"company":empresa,"announcement":anuncio,"description":desc})],ignore_index=True)
    except:
      break
    cont +=10

df = df.drop_duplicates(subset=['description'])
df = df.reset_index(drop=True)

