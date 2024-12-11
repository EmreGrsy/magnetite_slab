from cProfile import label
from turtle import color, width
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font = {"size": 22}
plt.rc("font", **font)
plt.rc("legend",fontsize=16)

bench = pd.read_csv("benchmark.txt", sep="\s+", header=None)

# Fe(2+)-Fe(3+) of global min
bench.columns = ["core", "timestep_per_second"]

fig, axs = plt.subplots(1, sharex=True)

#fe3fe3_nvt["RDF"] = fe3fe3_nvt["RDF"] + 3
#fe3fe3_nvt_1e5["RDF"] = fe3fe3_nvt_1e5["RDF"] + 3.5

# Plot main NVT part of global min.
axs.plot(bench["core"], 1/bench["timestep_per_second"], "-x", linewidth=2)



# Define label
axs.set_xlabel(r"core",labelpad=12, fontsize=24)
axs.set_ylabel(r"second / step",labelpad=12, fontsize=24)
##ax1.text(0.99, 0.95, '(a)',verticalalignment='top', horizontalalignment='right',transform=ax1.transAxes)
#ax2.text(0.99, 0.95, '(b)',verticalalignment='top', horizontalalignment='right',transform=ax2.transAxes)

#ax1.legend(bbox_to_anchor=(0.5, 1.36), framealpha=0.0, ncol=2, loc='center')

#fig.text(-0.05, 0.5, r"$g\,(r)$", va='center', rotation='vertical')

fig.savefig('benchmark.pdf',format='pdf', bbox_inches = "tight")
fig.savefig('benchmark.png',dpi=300.0,format='png', bbox_inches = "tight")
