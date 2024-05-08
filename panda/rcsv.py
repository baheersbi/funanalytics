import pandas as pd
import json
# data = pd.read_csv('../data/data.csv')
# dt = pd.read_json('../data/data.json')
# data = pd.read_json('../data/data.json')
with open("../data/data.json") as json_file:
    json_data = json.load(json_file)
    print(json.dumps(json_data, indent=4))
# parsed = json.loads(dt)
# print(json.dumps(parsed, indent=4))