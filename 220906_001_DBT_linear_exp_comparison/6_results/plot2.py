from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter, NullFormatter

font = {"size"   : 24}
plt.rc("font", **font)


df = pd.read_csv("pe_comp_4.txt", header=None, delimiter=" ", comment='#')
df.columns =["layer","ordered_swp","ordered_min","exp_swp_new", "exp_min_new","exp_swp_old", "exp_min_old", "natom", "RandomAvg", "RandomStd"]

# Delta E - E
#df["dE_swp_new"] = df["ordered_swp"]-df["exp_swp_new"]
#df["dE_min_new"] = df["ordered_min"]-df["exp_min_new"]

#df["dE_swp_old"] = -df["ordered_swp"]+df["exp_swp_old"]
df["dE_min_old"] = -df["ordered_min"]+df["exp_min_old"]

#df["dE_random"] = df["ordered_min"]-df["RandomAvg"]


# Change units from kcal/mol to eV/atom
#df["dE_swp_new"] = (df["dE_swp_new"].apply(lambda x: x*0.0433634))/df["natom"]
#df["dE_min_new"] = (df["dE_min_new"].apply(lambda x: x*0.0433634))/df["natom"]

#df["dE_swp_old"] = (df["dE_swp_old"].apply(lambda x: x*0.0433634))/df["natom"]
df["dE_min_old"] = (df["dE_min_old"].apply(lambda x: x*0.0433634))/df["natom"]

#df["dE_random"] = (df["dE_random"].apply(lambda x: x*0.0433634))/df["natom"]

#df["RandomStd"] = (df["RandomStd"].apply(lambda x: x*0.0433634))/df["natom"]


fig, axs = plt.subplots(1, sharex=True)

#axs.plot(df["layer"], df["dE_ordered_swp"],"red" ,linewidth=4, label=r"$\tilde{E} - E^\mathrm{exp}$")
#axs.plot(df["layer"], df["dE_ordered_min"],"blue" ,linewidth=4, label=r"$\tilde{E}- E^\mathrm{lin}$")
#axs.plot(df["layer"], df["dE_exp_swp"],"blue" ,linewidth=4, label=r"$\tilde{E}- E^\mathrm{exp,new}$")
#axs.plot(df["layer"], df["dE_exp_min"],"blue" ,linewidth=4, label=r"$\tilde{E}- E^\mathrm{min}$")
#axs[0].plot(df["layer"], df["dE_swp_new"]*1000,"b" ,linewidth=3, label=r"$\tilde{E}_\mathrm{swp}-E^\mathrm{min}_\mathrm{swp}$")
#axs[1].plot(df["layer"], df["dE_min_new"]*1000,"b" ,linewidth=3, label=r"$\tilde{E}-E_\mathrm{new}$")

#axs.plot(df["layer"], df["dE_swp_old"]*1000,"b--" ,linewidth=3, label=r"$\Delta E_\mathrm{min}$", zorder=2)
axs.plot(df["layer"], df["dE_min_old"]*1000,"b" ,linewidth=3, 
         label=r"$\Delta E_\mathrm{min}$", zorder=2)

#axs[1].plot(df["layer"], df["dE_random"]*1000,"r" ,linewidth=3, label=r"$\tilde{E}-E_\mathrm{random}$")

#error = df["RandomStd"]*1000
#axs[1].errorbar(df["layer"], df["dE_random"]*1000,yerr=error, color="red", linewidth=3)

#axs[1].plot(df["layer"], df["dE_random"]*1000,"r" ,linewidth=3, label=r"$\tilde{E}-E_\mathrm{random}$")

axs.set_xlim([0, 45])
axs.set_xticks([10, 25, 40])
#axs.set_ylim([-5,12])
#axs.set_yticks([ -2, -1, 0 , 1])

#fig.set_ylabel(r"$\Delta E$ (meV/atom)",labelpad=12)

#fig.text(-0.1, 0.5, r"$\Delta E$ (meV/atom)", va='center', rotation='vertical')
axs.legend(framealpha=0.0, loc='best', fontsize=20)

#axs.text(0.99, 0.93, r'$(MC)$',verticalalignment='top', horizontalalignment='right',transform=axs[0].transAxes)
#axs[1].text(0.99, 0.33, r'$(Relax)$',verticalalignment='top', horizontalalignment='right',transform=axs[1].transAxes)

axs.axvline(x=25, color="black", ymax=0.9, ls="--", linewidth=2)
axs.axhline(y=0, color="black", xmax=1, ls="--", linewidth=2, zorder=1)

axs.set_ylabel(r"$\Delta E$ (meV/atom)",labelpad=22)
axs.set_xlabel("Atomic layers",labelpad=22)
#axs[1].legend(frameon=False, fontsize=12)

fig.savefig('surface_comparison_after25_v2.pdf',format='pdf', bbox_inches = "tight")
fig.savefig('surface_comparison_after25_v2.png', dpi=300.0,format='png', bbox_inches = "tight")
