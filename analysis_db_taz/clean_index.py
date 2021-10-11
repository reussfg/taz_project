import csv
import pandas as pd
year = [x for x in range(2010, 2022)]

for k in year:
    with open(f'/Users/gabrielreus/Desktop/TAZ/client_data_base/Years/db_read/new_date/{k}-new.csv', 'r', encoding= "utf-8") as f:
        csv_reader = csv.reader(f)
        list_of_rows = list(csv_reader)
        list_of_rows.pop(0)
        for y in list_of_rows:
            y.pop(4)

    df = pd.DataFrame(list_of_rows)
    df.to_csv(f'{k}-clean.csv', index=False, header=False, encoding= "utf-8")
        