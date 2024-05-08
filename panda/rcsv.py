import pandas as pd
import json
# data = pd.read_csv('../data/data.csv')
# dt = data.to_json('../data/data.json')
data = pd.read_json('../data/data.json')
print(data)
