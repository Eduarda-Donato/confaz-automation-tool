from data_loader import dataload_month
from excel_writter import write_to_excel


def process_data(CONFAZ_MONTH_PATH, NEW_CONFAZ_FILE, MES_ANO, CONFAZ_FILE):
    try:
        df_month = dataload_month(CONFAZ_MONTH_PATH)
        write_to_excel(df_month, NEW_CONFAZ_FILE, MES_ANO, CONFAZ_FILE)
        
    except Exception as e:
        print("Ocorreu um erro ao processar os dados:")
        print(e)