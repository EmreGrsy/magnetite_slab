import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams


font = {'size'   : 24}
plt.rc('font', **font)
plt.rc("legend",fontsize=18)
rcParams['axes.titlepad'] = 20 

df = pd.read_csv("info.data", header=None, delimiter=" ")
df = df.T  # Transpose df, now mc_temp is columns and layers are rows
df["layer"] = df.index

for mc_temp in range(len(df.columns)-1):

    fig, axs = plt.subplots()

    axs.plot(df[mc_temp][1:]/36, df.layer[1:], linewidth=3, color="blue", label=df[0][0])

    axs.set_ylim(axs.get_ylim()[::-1])  # Inverse y-axis

    axs.set_xlim([-0.25, 1.25])

    axs.set_yticks([0,5,10,15, 20, 25, 30, 40])

    legend = r"$T^\mathrm{MC}$ = %iK" % df[mc_temp][0]
    #axs.legend()
    axs.text(-0.18, 2.5, legend, fontsize=18, color="blue")

    axs.set_title("21L surface on 22L bulk", fontsize=24)

    axs.set_ylabel(r"Fe$_\mathrm{oct}$ layer", ha="center", fontsize=24, labelpad=10)
    axs.set_xlabel(r"$\frac{N_{\mathrm{{Fe}_{oct}^{III}}}}{N_{\mathrm{{Fe}_{oct}^{III}}}+N_{\mathrm{{Fe}_{oct}^{II}}}}$", ha="center", fontsize=24, labelpad=10)

    fig.patch.set_facecolor("white")
    fig.savefig('1_ratio_figs/fe3oct_%i.png' %mc_temp, dpi=300.0,format='png', bbox_inches = "tight")

#fig.savefig('fe3_oct_ratio_half_tet.pdf',format='pdf', bbox_inches = "tight")
#fig.savefig('fe3_oct_.png', dpi=300.0,format='png', bbox_inches = "tight")
