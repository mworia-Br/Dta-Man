import pandas as pd

column = ["Bray","Batman","Spongebob"]
titled_column = {"name": column}
data = pd.DataFrame(column)
print(data)