import pandas as pd

# a = [2, 4, 9, 8, 8, 9, 23, 70]
# sum = 0
# for x in a:
#     if x == 23:
#         continue
#     sum = sum + x
# print(sum)
# myseries = pd.Series(a, index = ["j", "k", "l", "m", "n", "o", "p", "q"])
# myseries = pd.Series(a)
# c = myseries[2]+myseries[6]

# print(sum(myseries))
# print(max(myseries))
# print(min(myseries))
# print(myseries.mean())
# print(myseries.min())
# print(myseries.std())
# print(myseries.var())
# print(myseries[7])

# print(myseries)


#Key:Value Pairs of Data

# calories = {
#             "day1": 420,
#             "day2": 380,
#             "day3": 390
#             }
# print(calories)
# myseries = pd.Series(calories, index= ["day1", "day2"])
# print(myseries)

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
    # "names": ['Ali', 'Mark', 'Carlos']
}
myvar = pd.DataFrame(data)
print(myvar)
print("---------------------")
# print(myvar.loc[2])
# print(myvar.calories[1])
# print(myvar.loc[2].values[1])
print(myvar.loc[[0,2]])
