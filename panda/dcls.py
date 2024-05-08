import pandas as pd

data = pd.read_csv('../data/data.csv')
# pd.set_option('display.max_rows', data.shape[0]+1)

# print(data)
# empty_cells = data.isna()
# # empty_rows = empty_cells[empty_cells.isnull().all(axis=1)]
# print(empty_cells)
# print(data.info())
# print(data.head(10))
# print("---------------------------")
# print(data.tail(10))

#
# print("Totol Records:" + str(data.count()))
# data.dropna()
# new_data = data.dropna(inplace=True)
# print("Records after deletion:" + str(new_data.count()))
# print(new_data.to_string())

# print("Totol Records:" + str(data.count()))
average_cal = data.Calories.mean()
average_maxpulse = data.Maxpulse.mean()
data["Calories"].fillna(round(average_cal), inplace = True)
data["Maxpulse"].fillna(round(average_maxpulse), inplace = True)
# print(round(average_dt))
data.fillna(round(average_dt), inplace = True)
print("How many records are affected:" + str(data.count()))
print(data.to_string())


