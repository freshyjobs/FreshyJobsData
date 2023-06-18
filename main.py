import pandas as pd

#read Json data from local and concat no use
# localDF = pd.read_json('data/data.json')
# df3 = pd.concat([localDF, gSheetDF])

#Read JSON data and Write a json file for github upload
SHEET_ID = '1Z8xJbCChI94kgMb5js1my3dbKM3_4Upd'
SHEET_NAME = 'master'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
gSheetDF = pd.read_csv(url)

gSheetDF.to_json(r'data/data2.json',orient='records')