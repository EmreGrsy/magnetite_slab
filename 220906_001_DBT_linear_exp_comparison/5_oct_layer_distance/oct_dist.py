from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import StrMethodFormatter, NullFormatter

font = {"size"   : 24}
plt.rc("font", **font)


df = pd.read_csv("slab_oct_dist_analysis.txt", header=None, delimiter=" ", comment='#')
df.columns =["layer","dist_min", "dist_ave", "dist_max", "mid_dist", "ave_center", "thickness"]

fig, axs = plt.subplots(1)

axs.plot(df["layer"], df["thickness"]/((df["layer"]+1)/2), "b", linewidth=3, label="(001)-DBT")

axs.axhline(y=(25.403165817260742/12), color="black", xmax=1, ls="--", linewidth=3, label="Bulk")

#axs.axhline(y=(25.403165817260742/2.119999972256747), color="black", xmax=1, ls="--", linewidth=3, label="Ideal lattice")

#max_err = df.dist_max.values-df.dist_ave.values
#min_err = df.dist_ave.values-df.dist_min.values

axs.set_xlim([0,45])

axs.set_xticks([10, 25, 40])

#axs.errorbar(df["thickness"]/10, df["dist_ave"], yerr=np.vstack((min_err, max_err)), ecolor="blue")

axs.legend(framealpha=0.0, ncol=1, loc='upper left', fontsize=20)

axs.set_xlabel(r"Layer",labelpad=12, fontsize=24)
#axs.set_ylabel(r"$\dfrac{{\Delta L}}{\Delta d_\mathrm{oct}}$",labelpad=12, fontsize=24)
axs.set_ylabel(r"$d_\mathrm{oct} \, (\AA)$",labelpad=12, fontsize=24)

fig.savefig("lavg_oct_dist.pdf",format="pdf", bbox_inches = "tight")
fig.savefig("lavg_oct_dist.png",dpi=300.0,format="png", bbox_inches = "tight")
