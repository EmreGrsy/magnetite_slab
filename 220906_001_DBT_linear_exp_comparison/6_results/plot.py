from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter, NullFormatter

font = {"size"   : 24}
plt.rc("font", **font)


df = pd.read_csv("pe_comp2.txt", header=None, delimiter=" ")
df.columns =["layer","charge_ordered","linear","exp", "exp2"]

# Change units from kcal/mol to eV
df["charge_ordered"] = df["charge_ordered"].apply(lambda x: x*0.0433634)
df["linear"] = df["linear"].apply(lambda x: x*0.0433634)
df["exp"] = df["exp"].apply(lambda x: x*0.0433634)
df["exp2"] = df["exp2"].apply(lambda x: x*0.0433634)

df["dE_linear"] = df["linear"]-df["charge_ordered"]
df["dE_exp"] = df["exp"]-df["charge_ordered"]
df["dE_exp2"] = df["exp2"]-df["charge_ordered"]

fig,axs = plt.subplots()

axs.plot(df["layer"], df["dE_exp"],"red" ,linewidth=4, label=r"$\tilde{E} - E^\mathrm{exp}$")
axs.plot(df["layer"], df["dE_linear"],"blue" ,linewidth=4, label=r"$\tilde{E}- E^\mathrm{lin}$")
axs.plot(df["layer"], df["dE_exp2"],"green" ,linewidth=4, label=r"$\tilde{E}- E^\mathrm{exp2}$")

#axs.set_xlim([15,45])
axs.set_xticks([20, 25, 30, 35, 40])
axs.set_ylim([-2,1.5])
#axs.set_yticks([ -2, -1, 0 , 1])

axs.set_ylabel(r"$\Delta E$ (eV)",labelpad=12)

axs.axvline(x=25, color="black", ymax=1, ls="--", linewidth=2.5)

axs.set_xlabel("Atomic layer",labelpad=22)
axs.legend(frameon=False, fontsize=18)

fig.savefig('surf_sa_analysis_2.pdf',format='pdf', bbox_inches = "tight")
fig.savefig('surf_sa_analysis_2.png', dpi=300.0,format='png', bbox_inches = "tight")