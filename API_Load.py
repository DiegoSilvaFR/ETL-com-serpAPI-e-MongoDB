from pymongo import MongoClient
import pandas as pd
from API_ET import df

print(df)

password = 2357       #sua senha do mongoDB
url = f'mongodb+srv://diego:{password}@cluster.nf0lbzp.mongodb.net/?retryWrites=true&w=majority'
cliente = MongoClient(url)

dbs = cliente.list_database_names()
print(dbs) #databases criados

DB = cliente.project
DB.project.delete_many({}) #isso irá excluir a coleção para ser atualizada

def insert_values(df):
  collection = DB.new

  colec = []
  for i in range(len(df)):
    doc = {"title":df.loc[i].title,"company":df.loc[i].company,"announcement":df.loc[i].announcement,"description":df.loc[i].description}
    colec.append(doc)
  collection.insert_many(colec)

insert_values(df)