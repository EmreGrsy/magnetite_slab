import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

font = {"size"   : 24}
plt.rc("font", **font)

df = pd.read_csv("min.txt", header=None, delimiter=" ")
df.columns =["17L","21L","25L","29L", "33L","37L", "41L"]

df["17L"] = -215992.16 - df["17L"]
df["21L"] = -263545.40 - df["21L"]
df["25L"] = -311098.56 - df["25L"]
df["29L"] = -358651.71 - df["29L"]
df["33L"] = -406204.96 - df["33L"]
df["41L"] = -501327.69 - df["41L"]

