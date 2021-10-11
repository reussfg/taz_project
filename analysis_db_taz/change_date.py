import csv
import pandas as pd
year = [x for x in range(2010, 2022)]

for k in year:
    with open(f'/Users/gabrielreus/Desktop/TAZ/client_data_base/Years/db_read/new_date/{k}-clean.csv', 'r', encoding= "utf-8") as f:
        csv_reader = csv.reader(f)
        list_of_rows = list(csv_reader)
        for x in list_of_rows:
            x[2] = k

    df = pd.DataFrame(list_of_rows)
    df.to_csv(f'{k}-new_year.csv', index=False, header=False, encoding= "utf-8")