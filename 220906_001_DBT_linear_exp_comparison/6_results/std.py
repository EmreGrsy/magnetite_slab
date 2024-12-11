import pandas as pd

df = pd.read_csv("std_25L.data", header=None, delimiter=" ")
df.columns =["swp","min"]

