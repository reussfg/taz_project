import pandas as pd
import csv

year = [x for x in range(2010, 2022)]
for k in year:

# Transform from xlsx to csv
    excel_read = pd.read_excel(rf'/Users/gabrielreus/Desktop/TAZ/client_data_base/Years/{k}/{k}.xlsx')
    excel_read.to_csv (rf'/Users/gabrielreus/Desktop/TAZ/client_data_base/Years/{k}/{k}.csv', index = None, header = True, encoding= "utf-8")

    with open(f'/Users/gabrielreus/Desktop/TAZ/client_data_base/Years/{k}/{k}.csv', 'r') as f:
        csv_reader = csv.reader(f)
        list_of_rows = list(csv_reader)
        copy = []
        copy2 = []
        for x in list_of_rows:
            for y in x[:]:
                if y.strip():
                    copy.append(y)
        for x in copy:
            x = x.replace(',', '')
            copy2.append(x)
        copy3 = []
        parametro = []
        contador = 0
        while contador != len(copy2):
            if contador % 7 == 0 and contador != 0:
                copy3.append(parametro)
                parametro = []
            parametro.append(copy2[contador])
            contador += 1
        df = pd.DataFrame(copy3)
        df.to_csv(f'{k}-new.csv', index=False, header=False, encoding= "utf-8")
