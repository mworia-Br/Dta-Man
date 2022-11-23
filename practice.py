import pandas as pd

column = ["Bray","Batman","Spongebob"] #list
titled_columns = {"Name": column,
                 "Height": [1.7, 1.9, 0.25],
                 "Weight": [62, 100, 1] }
data = pd.DataFrame(titled_columns)
select_column = data["Weight"] # Selects entire column Weight
print(data)
print(select_column)