import os
import pandas as pd 


CONFAZ_PATH = "S:\\GET\\Geral\\EDUARDA DONATO\\GOBF\\CONFAZ 2025\\mmmm"

data = []
colunas = ['ITEM','ESPÉCIE','NÚMERO','DATA','PUBLICAÇÃO D.O.E','TERMO INICIAL','TERMO FINAL','ESPECIFICAÇÃO  BENEFÍCIO','TIPO','CNPJ/CPF','RAZÃO SOCIAL/NOME','ENQUADRAMENTO','ATO NORMATIVO','OBSERVAÇÕES']


for subfolder in os.listdir(CONFAZ_PATH):
    subfolder_path = os.path.join(CONFAZ_PATH, subfolder)
    #print(subfolder_path)
    if os.path.isdir(subfolder_path) and any(x in subfolder for x in ["DOC", "DECRETO", "LEI"]):
        for file in os.listdir(subfolder_path):
            #print(path)
            if file.endswith(".xls") or file.endswith(".xlsx"):
                file_path = os.path.join(subfolder_path, file)
                #print(file_path)
                
                
                df = pd.read_excel(file_path, skiprows=5, engine="xlrd")#,names=colunas)
                
                print(df.head())
                #data.append(df)
                
                
                
                
                
                
#df_final = pd.concat(todos_dados, ignore_index=True)
#df_final.to_excel(r"C:\caminho\para\saida\dados_juntos.xlsx", index=False)
#print("Arquivos combinados com sucesso!")