import pandas as pd

#creating dataframe

column = ["Bray","Batman","Spongebob"]          #list
titled_columns = {"Name": column,
                 "Height": [1.7, 1.9, 0.25],
                 "Weight": [62, 100, 1] }       #Dictionary
data = pd.DataFrame(titled_columns)

#selecting values from dataframe

select_column = data["Weight"]       # Selects entire column Weight
select_column1 = data["Weight"][1]   # Selects index 1 in column Weight

select_row = data.iloc[2]            # select entire row at index 2
select_row2 = data.iloc[2]["Weight"] #selects a single value of weight from row at index 2

#Manipulating dataframe values
bmi = []
# formulae is weight/(height**2)
for i in range(len(data)):           # bmi calc logic
    bmi_score = data["Weight"][i]/(data['Height'][i]**2)
    bmi.append(bmi_score)

data["bmi"] = bmi

print(data)
#print(select_column)
#print(select_column1)
#print(select_row)
#print(select_row2)