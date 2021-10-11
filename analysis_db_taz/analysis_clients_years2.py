import pandas as pd
import csv


with open(f'/Users/gabrielreus/Desktop/TAZ/client_data_base/Years/merged.csv', 'r') as f:
    csv_reader = csv.reader(f)
    list_of_rows = list(csv_reader)
    store1 = []
    store2 = []
    for k in list_of_rows:
        if k[2] == '2020':
            store1.append(k[1])
        else:
            store2.append(k[1])

    uni1 = pd.unique(store1).tolist()
    uni2 = pd.unique(store2).tolist()
    lost = list(set(uni1) - set(uni2))

    textfile = open('Perdido-total.txt', 'w')
    for element in lost:
        textfile.write((element + '\n'))
    textfile.close()



