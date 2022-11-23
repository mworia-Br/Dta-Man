import pandas as pd

column = ["Bray","Batman","Spongebob"]
titled_column = {"name": column}
data = pd.DataFrame(titled_column)
print(data)