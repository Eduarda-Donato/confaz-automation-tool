import os
import pandas as pd

DOC_TYPE = ["DOC", "DECRETO", "LEI"]

def dataload_month(month_path: str) -> pd.DataFrame:
    df_month = None

    for subfolder in os.listdir(month_path):
        subfolder_path = os.path.join(month_path, subfolder)

        if os.path.isdir(subfolder_path) and any(x in subfolder for x in DOC_TYPE):
            for file in os.listdir(subfolder_path):
                if file.endswith((".xls", ".xlsx")):
                    file_path = os.path.join(subfolder_path, file)
                    try:
                        df = pd.read_excel(file_path, sheet_name="ATOS CONCESSIVOS", skiprows=5)
                    except ValueError:
                        df = pd.read_excel(file_path, sheet_name="VERSÃO ANTERIOR", skiprows=5)
                    
                    if df_month is None:
                        df_month = df
                    else:
                        df_month = pd.concat([df_month, df], ignore_index=True)

    return df_month