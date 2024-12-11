#from matplotlib.lines import _LineStyle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter, NullFormatter, AutoMinorLocator
from matplotlib import rcParams

files = [
    "17L_linear_info.data",
    "21L_linear_info.data",
    "25L_info.data",
    "29L_info.data",
    "33L_info.data",
    "37L_info_2.data",
    "41L_info.data",
    "13L_scv_info.data",
    "17L_scv_info.data"
]

df_names = [
    "df_17L",
    "df_21L",
    "df_25L",
    "df_29L",
    "df_33L",
    "df_37L",
    "df_41L",
    "df_13L_scv",
    "df_17L_scv"
]

df_list = []

font = {'size'   : 18}
plt.rc('font', **font)
plt.rc("legend",fontsize=24)
rcParams['axes.titlepad'] = 3 

#plt.rcParams['axes.titlepad'] = -10

for i in range(len(files)):
    tmp_df = pd.read_csv(files[i], sep="\s+",
    names = ["layer", "nfe3", "nfe2", "ntotal"])
    df_list.append(tmp_df)
    df_list[i]["rfe3"] = df_list[i]["nfe3"] / df_list[i]["ntotal"]

fig, axs = plt.subplots(1, 7, figsize=(15, 6), facecolor="w", 
                         sharex=True, sharey=True)

fig.subplots_adjust(wspace=0.1)

axs[0].set_xlim([-0.15, 1.15])
axs[0].set_ylim([0, 22])

axs[0].set_yticks(range(1, 25, 4))
axs[0].set_xticks([0, 1])

ml = AutoMinorLocator(2)
axs[0].xaxis.set_minor_locator(ml)

ml = AutoMinorLocator(4)
axs[0].yaxis.set_minor_locator(ml)

axs[0].invert_yaxis()

axs[0].plot(df_list[0]["rfe3"], df_list[0]["layer"], linewidth=4, label="17", color="blue")
axs[1].plot(df_list[1]["rfe3"], df_list[1]["layer"], linewidth=4, label="21", color="blue")
axs[2].plot(df_list[2]["rfe3"], df_list[2]["layer"], linewidth=4, label="25", color="blue")
axs[3].plot(df_list[3]["rfe3"], df_list[3]["layer"], linewidth=4, label="29", color="blue")
axs[4].plot(df_list[4]["rfe3"], df_list[4]["layer"], linewidth=4, label="33", color="blue")
axs[5].plot(df_list[5]["rfe3"], df_list[5]["layer"], linewidth=4, label="37", color="blue")
axs[6].plot(df_list[6]["rfe3"], df_list[6]["layer"], linewidth=4, label="41", color="blue")

axs[0].set_title("17L", fontsize=24, pad=15)
axs[1].set_title("21L", fontsize=24, pad=15)
axs[2].set_title("25L", fontsize=24, pad=15)
axs[3].set_title("29L", fontsize=24, pad=15)
axs[4].set_title("33L", fontsize=24, pad=15)
axs[5].set_title("37L", fontsize=24, pad=15)
axs[6].set_title("41L", fontsize=24, pad=15)

for x in range(7):
    axs[x].grid(color='gray', linestyle='dotted', alpha=0.5, which="minor")
    axs[x].grid(color='gray', linestyle='dotted', alpha=0.5, which="major")

ax0 = fig.add_subplot(111, frame_on=False)
ax0.set_xticks([])
ax0.set_yticks([])
ax0.set_xlabel(r"$n_\mathrm{Fe_{oct}^{3+}} / n_\mathrm{Fe_{oct}}}$", labelpad=45, fontsize=24)
ax0.set_ylabel(r"Fe$_\mathrm{oct}$ layer", labelpad=55, fontsize=24)

""" axs[2,0].plot(df_list[6]["layer"], df_list[6]["rfe3"], linewidth=3, label="41", color="blue")
axs[2,1].plot(df_list[7]["layer"], df_list[7]["rfe3"], linewidth=3, label="13_scv", color="blue")
axs[2,2].plot(df_list[8]["layer"], df_list[8]["rfe3"], linewidth=3, label="17_scv", color="blue")

axs[0,1].tick_params(direction="inout", axis="y", length=3)
axs[0,2].tick_params(direction="inout", axis="y", length=3)

axs[1,1].tick_params(direction="inout", axis="y", length=3)
axs[1,2].tick_params(direction="inout", axis="y", length=3)

axs[2,1].tick_params(direction="inout", axis="y", length=3)
axs[2,2].tick_params(direction="inout", axis="y", length=3)

axs[0,0].set_xlim([0,10])
axs[0,1].set_xlim([0,12])
axs[0,2].set_xlim([0,14])
axs[1,0].set_xlim([0,16])
axs[1,1].set_xlim([0,18])
axs[1,2].set_xlim([0,20])
axs[2,0].set_xlim([0,22])
axs[2,1].set_xlim([0,8])
axs[2,2].set_xlim([0,10])

axs[0,0].set_ylim([-0.1,1.1])
axs[0,1].set_ylim([-0.1,1.1])
axs[0,2].set_ylim([-0.1,1.1])
axs[1,0].set_ylim([-0.1,1.1])
axs[1,1].set_ylim([-0.1,1.1])
axs[1,2].set_ylim([-0.1,1.1])
axs[2,0].set_ylim([-0.1,1.1])
axs[2,1].set_ylim([-0.1,1.1])
axs[2,2].set_ylim([-0.1,1.1])

axs[0,0].set_xticks([1,3,5,7,9])
axs[0,1].set_xticks([1,3,5,7,9,11])
axs[0,2].set_xticks([1,3,5,7,9,11,13])
axs[1,0].set_xticks([1,3,5,7,9,11,13,15])
axs[1,1].set_xticks([1,3,5,7,9,11,13,15,17])
axs[1,2].set_xticks([1,3,5,7,9,11,13,15,17,19])
axs[2,0].set_xticks([1,3,5,7,9,11,13,15,17,19,21])
axs[2,1].set_xticks([1,2,3,4,5,6,7])
axs[2,2].set_xticks([1,2,3,4,5,6,7,8,9])

axs[0,0].title.set_text("(001)-DBT-17L")
axs[0,1].title.set_text("(001)-DBT-21L")
axs[0,2].title.set_text("(001)-DBT-25L")
axs[1,0].title.set_text("(001)-DBT-29L")
axs[1,1].title.set_text("(001)-DBT-33L")
axs[1,2].title.set_text("(001)-DBT-37L")
axs[2,0].title.set_text("(001)-DBT-41L")
axs[2,1].title.set_text("(001)-SCV-13L")
axs[2,2].title.set_text("(001)-SCV-17L")

axs[0,1].set_yticklabels([])
axs[0,2].set_yticklabels([])
axs[1,1].set_yticklabels([])
axs[1,2].set_yticklabels([])
axs[2,0].set_yticks([0.0, 0.5, 1.0])
axs[2,1].set_yticks([0.0, 0.5, 1.0])
axs[2,2].set_yticks([0.0, 0.5, 1.0])
axs[2,1].set_yticklabels([])
axs[2,2].set_yticklabels([]) """

#fig.delaxes(axs[2,0])
#fig.delaxes(axs[2,2])

#fig.supxlabel(r"Fe$_\mathrm{oct}$ layer", fontsize=14)
#fig.supylabel(r"$\frac{N_{\mathrm{{Fe}_{oct}^{III}}}}{N_{\mathrm{{Fe}_{oct}^{III}}}+N_{\mathrm{{Fe}_{oct}^{II}}}}$", fontsize=14)

#fig.text(0.5, -0.01, r"Fe$_\mathrm{oct}$ layer", ha="center", fontsize=14)
#fig.text(0.02, 0.42, r"$\frac{N_{\mathrm{{Fe}_{oct}^{III}}}}{N_{\mathrm{{Fe}_{oct}^{III}}}+N_{\mathrm{{Fe}_{oct}^{II}}}}$", ha="center", fontsize=14, rotation=90)

#fig.subplots_adjust(hspace=0.5,wspace = 0.05)

fig.savefig('fe3_oct_ratio_DBT1.pdf',format='pdf', bbox_inches = "tight")
fig.savefig('fe3_oct_ratio_DBT1.png', dpi=300.0,format='png', bbox_inches = "tight")
