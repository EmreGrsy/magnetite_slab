from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter, NullFormatter

font = {"size"   : 24}
plt.rc("font", **font)


df = pd.read_csv("pe_comp_3.txt", header=None, delimiter=" ", comment='#')
df.columns =["layer","ordered_swp","ordered_min","exp_swp_new", "exp_min_new","exp_swp_old", "exp_min_old", "natom"]

# Change units from kcal/mol to eV
df["ordered_swp"] = df["ordered_swp"].apply(lambda x: x*0.0433634)
df["ordered_min"] = df["ordered_min"].apply(lambda x: x*0.0433634)

df["exp_swp_new"] = df["exp_swp_new"].apply(lambda x: x*0.0433634)
df["exp_min_new"] = df["exp_min_new"].apply(lambda x: x*0.0433634)
df["exp_swp_old"] = df["exp_swp_old"].apply(lambda x: x*0.0433634)
df["exp_min_old"] = df["exp_min_old"].apply(lambda x: x*0.0433634)

#df["dE_ordered_swp"] = df["ordered_swp"]-df["ordered_swp"]
#df["dE_ordered_min"] = df["ordered_min"]-df["ordered_min"]
#df["dE_exp_swp"] = df["exp_swp"]-df["ordered_swp"]
#df["dE_exp_min"] = df["exp_min"]-df["ordered_min"]

df["dE_swp2"] = (df["exp_swp_new"]-df["exp_swp_old"])/df["natom"]
df["dE_min2"] = (df["exp_min_new"]-df["exp_min_old"])/df["natom"]

fig,axs = plt.subplots()

#axs.plot(df["layer"], df["dE_ordered_swp"],"red" ,linewidth=4, label=r"$\tilde{E} - E^\mathrm{exp}$")
#axs.plot(df["layer"], df["dE_ordered_min"],"blue" ,linewidth=4, label=r"$\tilde{E}- E^\mathrm{lin}$")
#axs.plot(df["layer"], df["dE_exp_swp"],"blue" ,linewidth=4, label=r"$\tilde{E}- E^\mathrm{exp,new}$")
#axs.plot(df["layer"], df["dE_exp_min"],"blue" ,linewidth=4, label=r"$\tilde{E}- E^\mathrm{min}$")
axs.plot(df["layer"], df["dE_swp2"]*1000,"green" ,linewidth=4, label=r"$E^\mathrm{new}_\mathrm{swp}- E^\mathrm{old}_\mathrm{swp}$")
axs.plot(df["layer"], df["dE_min2"]*1000,"blue" ,linewidth=4, label=r"$E^\mathrm{new}_\mathrm{min}- E^\mathrm{old}_\mathrm{min}$")

#axs.set_xlim([15,45])
#axs.set_xticks([20, 25, 30, 35, 40])
#axs.set_ylim([-5,12])
#axs.set_yticks([ -2, -1, 0 , 1])

axs.set_ylabel(r"$\Delta E$ (meV/atom)",labelpad=12)

#axs.axvline(x=25, color="black", ymax=1, ls="--", linewidth=2.5)
axs.axhline(y=0, color="black", xmax=1, ls="--", linewidth=2.5)


axs.set_xlabel("Atomic layer",labelpad=22)
axs.legend(frameon=False, fontsize=18)

fig.savefig('surf_sa_analysis_3.pdf',format='pdf', bbox_inches = "tight")
fig.savefig('surf_sa_analysis_3.png', dpi=300.0,format='png', bbox_inches = "tight")
