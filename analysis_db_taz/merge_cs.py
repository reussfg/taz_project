import os, glob
import pandas as pd

path ='/Users/gabrielreus/Desktop/TAZ/client_data_base/Years/db_read/new_date/'
all_files = glob.glob(os.path.join(path, '*-new_year.csv'))
df_from_each_file = (pd.read_csv(f,sep=',') for f in all_files)
df_merged = pd.concat(df_from_each_file, ignore_index=True)
df_merged.to_csv = ('/Users/gabrielreus/Desktop/TAZ/client_data_base/Years/db_read/new_date/merged.csv')
