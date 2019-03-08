import pandas as pd 

#df = pd.read_html('https://tradingeconomics.com/united-states/gdp')
#print(df[-2]['Country'])

#df = pd.read_json(path_or_buf="full_hobro.json")
#print(df)

with open('full_hobro.json', 'rb') as f:
   data = f.readlines()
#print(data)

#
#data = map(lambda x: x.rstrip(), data)

#print(data)
data_json_str = "[" + ",".join(data) + "]"

data_df = pd.read_json(data_json_str)

print(data_df)