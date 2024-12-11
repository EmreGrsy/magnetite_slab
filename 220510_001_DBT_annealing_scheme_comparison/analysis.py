#from matplotlib.lines import _LineStyle
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter, NullFormatter

files = [
    "1000K_100K_full.log",
    "1000K_50K_full.log",
    "1000K_10K_full.log",
    "1000K_5K_full.log",
    "1000K_1K_full.log",
    "1000K_noAnnealing_full.log",
    "1000K_50K_half.log",
    "1000K_50K_quarter.log",
    "1000K_10K_half.log",
    "1000K_10K_quarter.log",
    "1000K_1K_half.log",
    "1000K_1K_quarter.log",
    "500K_50K_full.log",
    "500K_10K_full.log",
    "500K_1K_full.log"
]

df_names = [
    "df_1000K_100K_full",
    "df_1000K_50K_full",
    "df_1000K_10K_full",
    "df_1000K_5K_full",
    "df_1000K_1K_full",
    "df_1000K_noAnnealing_full",
    "df_1000K_50K_half",
    "df_1000K_50K_quarter",
    "df_1000K_10K_half",
    "df_1000K_10K_quarter",
    "df_1000K_1K_half",
    "df_1000K_1K_quarter",
    "df_500K_50K_full",
    "df_500K_10K_full",
    "df_500K_1K_full"
]

df_list = []

font = {'size'   : 20}
plt.rc('font', **font)

for i in range(len(files)):
    tmp_df = pd.read_csv(files[i], sep="\s+",
    names = ["timesteps", "temp", "pe", "mc_attempts", "mc_sucess", "fetet", "feoct"])
    df_list.append(tmp_df)


fig, axs = plt.subplots()

############------------Cooling temp. comparison-----------------################################################

# axs[1, 0].plot(df_list[0]["timesteps"]/1e6, df_list[0]["temp"], color="dodgerblue", linewidth=3, label="100K")
# axs[1, 0].plot(df_list[1]["timesteps"]/1e6, df_list[1]["temp"], color="darkorange", linewidth=3, label="50K")
# axs[1, 0].plot(df_list[2]["timesteps"]/1e6, df_list[2]["temp"], color="green", linewidth=3, label="10K")
# axs[1, 0].plot(df_list[3]["timesteps"]/1e6, df_list[3]["temp"], color="firebrick", linewidth=3, label="5K")
# axs[1, 0].plot(df_list[4]["timesteps"]/1e6, df_list[4]["temp"], color="mediumorchid", linewidth=3, label="1K")
# axs[1, 0].plot(df_list[5]["timesteps"]/1e6, df_list[5]["temp"], color="saddlebrown", linewidth=3, label="fixed")

# # Y-Label bottom row 
# axs[1, 0].set_ylabel("Temp. / K",labelpad=12)

# # Xticks
# axs[1,0].set_xticks([0, 2, 4, 6, 8])

# # Ylim
# axs[1,0].set_ylim([-100, 1100])

# ###### Inset
# axsin10 = axs[1,0].inset_axes([0.62, 0.65, 0.345, 0.325])

# axsin10.plot(df_list[0]["timesteps"]/1e6, df_list[0]["temp"], color="dodgerblue", linewidth=3, label="100K")
# axsin10.plot(df_list[1]["timesteps"]/1e6, df_list[1]["temp"], color="darkorange", linewidth=3, label="50K")
# axsin10.plot(df_list[2]["timesteps"]/1e6, df_list[2]["temp"], color="green", linewidth=3, label="10K")
# axsin10.plot(df_list[3]["timesteps"]/1e6, df_list[3]["temp"], color="firebrick", linewidth=3, label="5K")
# axsin10.plot(df_list[4]["timesteps"]/1e6, df_list[4]["temp"], color="mediumorchid", linewidth=3, label="1K")
# axsin10.plot(df_list[5]["timesteps"]/1e6, df_list[5]["temp"], color="saddlebrown", linewidth=3, label="fixed")

# axsin10.set_xlim([5.105, 5.190])
# axsin10.set_ylim([358, 373])

# axsin10.set_xticks([5.110, 5.17])

#axs[1,0].legend(loc="upper center", ncol=2, fancybox=True, bbox_to_anchor=(0.5, 1.3),  fontsize=5)
# ############------------Sample size comparison-----------------################################################

# axs[1, 1].plot(df_list[6]["timesteps"]/1e6, df_list[6]["temp"], linewidth=3, label="50K_half")
# axs[1, 1].plot(df_list[7]["timesteps"]/1e6, df_list[7]["temp"], linewidth=3, label="50K_quater")
# axs[1, 1].plot(df_list[8]["timesteps"]/1e6, df_list[8]["temp"], linewidth=3, label="10K_half")
# axs[1, 1].plot(df_list[9]["timesteps"]/1e6, df_list[9]["temp"], linewidth=3, label="10K_quarter")
# axs[1, 1].plot(df_list[10]["timesteps"]/1e6, df_list[10]["temp"], linewidth=3, label="1K_half")
# axs[1, 1].plot(df_list[11]["timesteps"]/1e6, df_list[11]["temp"], linewidth=3, label="1K_quarter")

# axs[1,1].set_ylim([0, 1100])

# axs[1,1].tick_params(axis="y", direction="in")

# axs[1,1].set_xticks([0, 0.50, 1,=20])

# ###### Inset
# axsin11 = axs[1,1].inset_axes([0.62, 0.65, 0.345, 0.325])

# axsin11.plot(df_list[6]["timesteps"]/1e6, df_list[6]["temp"], linewidth=3, label="50K_0.5")
# axsin11.plot(df_list[7]["timesteps"]/1e6, df_list[7]["temp"], linewidth=3, label="50K_0.25")
# axsin11.plot(df_list[8]["timesteps"]/1e6, df_list[8]["temp"], linewidth=3, label="10K_0.5")
# axsin11.plot(df_list[9]["timesteps"]/1e6, df_list[9]["temp"], linewidth=3, label="10K_0.25")
# axsin11.plot(df_list[10]["timesteps"]/1e6, df_list[10]["temp"], linewidth=3, label="1K_0.5")
# axsin11.plot(df_list[11]["timesteps"]/1e6, df_list[11]["temp"], linewidth=3, label="1K_0.25")

# axsin11.set_xlim([0.78, 0.795])
# axsin11.set_ylim([510, 522])

# axsin11.set_xticks([0.78, 0.79])

#axs[1,1].legend(loc="upper center", ncol=2, fancybox=True, bbox_to_anchor=(0.5, 1.3),  fontsize=5)

############------------Initial temp. comparison-----------------################################################

# axs[1, 2].plot(df_list[12]["timesteps"]/1e6, df_list[12]["temp"], linewidth=3, label="500K_50K")
# axs[1, 2].plot(df_list[13]["timesteps"]/1e6, df_list[13]["temp"], linewidth=3, label="500K_10K")
# axs[1, 2].plot(df_list[14]["timesteps"]/1e6, df_list[14]["temp"], linewidth=3, label="500K_1K")

# axs[1, 2].set_ylim([0, 1100])

# axs[1, 2].tick_params(axis="y", direction="in")

# ####### Inset

# axsin12 = axs[1, 2].inset_axes([0.5, 0.5, 0.445, 0.425])

# axsin12.plot(df_list[12]["timesteps"]/1e6, df_list[12]["temp"], linewidth=3, label="500K_50K")
# axsin12.plot(df_list[13]["timesteps"]/1e6, df_list[13]["temp"], linewidth=3, label="500K_10K")
# axsin12.plot(df_list[14]["timesteps"]/1e6, df_list[14]["temp"], linewidth=3, label="500K_1K")

# axsin12.set_xlim([0.5, 0.575])
# axsin12.set_ylim([430, 442])

# axsin12.set_xticks([])
# axsin12.set_yticks([])

# axs[1,2].indicate_inset_zoom(axsin12, edgecolor="black", alpha=0.5)

# #axs[1,2].legend(loc="upper center", ncol=2, fancybox=True, bbox_to_anchor=(0.5, 1.25),  fontsize=5)

############------------PE vs timestep-----------------################################################

axs.plot(df_list[0]["timesteps"]/0.8e6, df_list[0]["pe"]*0.00020415913, color="dodgerblue", linewidth=3, label="100K")
axs.plot(df_list[1]["timesteps"]/0.8e6, df_list[1]["pe"]*0.00020415913, color="darkorange", linewidth=3, label="50K")
axs.plot(df_list[2]["timesteps"]/0.8e6, df_list[2]["pe"]*0.00020415913, color="green", linewidth=3, label="10K")
axs.plot(df_list[3]["timesteps"]/0.8e6, df_list[3]["pe"]*0.00020415913, color="firebrick", linewidth=3, label="5K")
axs.plot(df_list[4]["timesteps"]/0.8e6, df_list[4]["pe"]*0.00020415913, color="mediumorchid", linewidth=3, label="1K")
axs.plot(df_list[5]["timesteps"]/0.8e6, df_list[5]["pe"]*0.00020415913, color="saddlebrown", linewidth=3, label="fixed")

axs.set_ylim([-82.419, -82.210])
axs.set_xlim([-0.1,10])

axs.set_xticks([0, 2, 4, 6, 8, 10])

axs.set_yticks([-82.40, -82.35, -82.30, -82.25, -82.20])

axs.set_ylabel("PE / eV/atom",labelpad=12)

axs.set_xlabel("Sample size  / $\mathrm{(Fe_{num})^2}$",labelpad=12)

axs.tick_params(axis="x", direction="in")

####### Inset
axsin00 = axs.inset_axes([0.65, 0.4, 0.30, 0.565])

axsin00.plot(df_list[0]["timesteps"]/0.8e6, df_list[0]["pe"]*0.00020415913, color="dodgerblue", linewidth=3, label="100K")
axsin00.plot(df_list[1]["timesteps"]/0.8e6, df_list[1]["pe"]*0.00020415913, color="darkorange", linewidth=3, label="50K")
axsin00.plot(df_list[2]["timesteps"]/0.8e6, df_list[2]["pe"]*0.00020415913, color="green", linewidth=3, label="10K")
axsin00.plot(df_list[3]["timesteps"]/0.8e6, df_list[3]["pe"]*0.00020415913, color="firebrick", linewidth=3, label="5K")
axsin00.plot(df_list[4]["timesteps"]/0.8e6, df_list[4]["pe"]*0.00020415913, color="mediumorchid", linewidth=3, label="1K")
axsin00.plot(df_list[5]["timesteps"]/0.8e6, df_list[5]["pe"]*0.00020415913, color="saddlebrown", linewidth=3, label="fixed")

axsin00.set_ylim([-82.4058, -82.3970])
axsin00.set_xlim([6,10.3])

axsin00.set_yticks([-82.4054,-82.4008,-82.3998])
#axsin00.set_xticks([5.12, 8.2])
axsin00.ticklabel_format(useOffset=False, style='plain')

axsin00.axhline(y=-82.4054, color="black", xmax=0.45, ls=":", linewidth=3)
axsin00.axhline(y=-82.4008, color="black", xmax=0.6, ls=":", linewidth=3)
axsin00.axhline(y=-82.3998, color="black", xmax=0.95, ls=":", linewidth=3)

#axsin00.get_yaxis().majorTicks[0].label1.set_horizontalalignment("")


axs.legend(loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.48,1.25), fontsize=20)

##########
# Glue plots together
fig.subplots_adjust(hspace=0.0,wspace = 0.0)

fig.savefig('sa_analysis.pdf',format='pdf', bbox_inches = "tight")
fig.savefig('sa_analysis.png', dpi=300.0,format='png', bbox_inches = "tight")