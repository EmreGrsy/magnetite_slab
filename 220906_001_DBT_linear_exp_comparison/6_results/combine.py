from turtle import color
import pandas as pd
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter, NullFormatter

font = {"size"   : 24}
plt.rc("font", **font)


######
df2 = pd.read_csv("7_oct_layer_distance/slab_oct_dist_analysis.txt", 
                  header=None, delimiter=" ")
df2.columns =["layer","dist_min", "dist_ave", 
              "dist_max", "mid_dist", "ave_center", 
              "thickness"]
######
df = pd.read_csv("pe_comp_4.txt", header=None, delimiter=" ", comment='#')
df.columns =["layer","ordered_swp","ordered_min","exp_swp_new", 
             "exp_min_new","exp_swp_old", "exp_min_old", "natom", 
             "RandomAvg", "RandomStd"]

df["dE_min_old"] = -df["ordered_min"] + df["exp_min_old"]
df["dE_min_old"] = (df["dE_min_old"].apply(lambda x: x*0.0433634))/df["natom"]


df["dE_swp_old"] = -df["ordered_swp"] + df["exp_swp_old"]
df["dE_swp_old"] = (df["dE_swp_old"].apply(lambda x: x*0.0433634))/df["natom"]



fig, axs = plt.subplots(3, sharex=True, figsize=(5,12))

axs[0].set_ylabel(r"$n_{\mathrm{Fe}}^\mathrm{2+}/n_{\mathrm{Fe}}^\mathrm{3+}$",
                  labelpad=22, fontsize=24)

axs[0].set_ylim([-0.25, 0.55])
axs[0].set_yticks([0.0, 0.25, 0.50])

axs[1].plot(df["layer"], df["dE_swp_old"]*1000, 
               "b" ,linewidth=4, ls="--",
               zorder=1, label="Swaps")

axs[1].plot(df["layer"], df["dE_min_old"]*1000,
            "b" ,linewidth=4, label="Swaps +" "\n" "lattice min.")


axs[1].axhline(y=0, color="black", xmax=1, ls=":", linewidth=3, zorder=1)
axs[1].legend(framealpha=0.0, ncol=1, loc='center left', fontsize=18)
axs[1].set_ylabel(r"$\Delta E$ (meV/atom)",labelpad=60)

#################

a = 1530  # nFeO
b = 780   # nFeT
c = 3120  # nO

p = 1.050 # qFe(II)
q = 1.575 # qFe(III)

#################
### (001)-dbt ###
#################

# create array with atoms in different thick slabs
nFeO = arange(864,0,-36)                     # nFeO
nFeT = arange(414,0,-18)                     # nFeT
nO   = arange(1728,0,-72)                    # O
nFeO = nFeO[:min([len(nFeO),len(nFeT),len(nO)])]
nFeT = nFeT[:min([len(nFeO),len(nFeT),len(nO)])]
nO   =   nO[:min([len(nFeO),len(nFeT),len(nO)])]
lz   = linspace(48.834,48.834-2.120*(len(nFeO)-1),len(nFeO))  # thickness of slab
l = linspace(47,3,23)

r = array([])
for a,b,c,d in zip(nFeO,nFeT,nO,l):
  # nFeT(II)/nFeT(III)
  y = arange(0,b+1,50)/float(b) 

  # nFeO(II)/nFeO(III)
  x = (-a*q -b*p*y +b*q*y -b*q +c*p) / (a*p - a*q)

  r = append(r,mean((a*x+b*y)/(a*(1.-x)+b*(1.-y))))

# plot data according to eq. in manuscript
axs[0].plot(l,r,label='(001)-DBT',color='red', linewidth=4)

# plot (111) dft results
#  on 001 with 13L we actually observed Fe2.5+
#  half of them is thus counted as 3+ and half 2+ 
nFe2_dft = array([4,8,12],dtype=float)
nFe3_dft = array([24,32,40],dtype=float)
lz_dft = array([9,13,17])

# New values from gregor 08.07.2022
nfe2_fe3_dft = array([0.3333])
lz2_dft = array([21])

axs[0].plot(lz_dft,nFe2_dft/nFe3_dft,'x',color='red', 
            markersize=3, markeredgewidth=12)
axs[0].plot(lz2_dft,nfe2_fe3_dft,'x',color='red', 
            markersize=3, markeredgewidth=12)


#################
### (111)-tet ###
#################

# create array with atoms in different thick slabs
nFeO = arange(1530,0,-120)                     # nFeO
nFeT = arange(780,0,-60)                       # nFeT
nO   = arange(3120,0,-240)                     # O
nFeO = nFeO[:min([len(nFeO),len(nFeT),len(nO)])]
nFeT = nFeT[:min([len(nFeO),len(nFeT),len(nO)])]
nO   =   nO[:min([len(nFeO),len(nFeT),len(nO)])]

#print "layers", (len(nFeO)-1,len(nFeO))
lz   = linspace(64.508,64.508-4.800*(len(nFeO)-1),len(nFeO))  # thickness of slab
l = linspace(77,5,13)

r = array([])
for a,b,c,d in zip(nFeO,nFeT,nO,l):
  # nFeT(II)/nFeT(III)
  y = arange(0,b+1,50)/float(b) 

  # nFeO(II)/nFeO(III)
  x = (-a*q -b*p*y +b*q*y -b*q +c*p) / (a*p - a*q)

  r = append(r,mean((a*x+b*y)/(a*(1.-x)+b*(1.-y))))

# plot data according to eq. in manuscript
axs[0].plot(l,r,label='(111)-tet',color='blue',linewidth=4)

# new 111 values from Gregor 08.07.2022
nfe2_nfe3_dft = array([0.1,0.214285714,0.277777778,0.318181818])
lz2_dft = array([11,17,23,29])

#P.plot(lz_dft,nFe2_dft/nFe3_dft,'x',color='C0')
axs[0].plot(lz2_dft,nfe2_nfe3_dft,'x',color='blue', 
            markersize=3, markeredgewidth=12)

#################
### (001)-scv ###
#################

# create array with atoms in different thick slabs
nFeO = arange(16,128,4)                    # nFeO
nFeT = arange(10,66,2)                     # nFeT
nO   = arange(40,264,8)                    # O

nFeO = nFeO[:min([len(nFeO),len(nFeT),len(nO)])]
nFeT = nFeT[:min([len(nFeO),len(nFeT),len(nO)])]
nO   =   nO[:min([len(nFeO),len(nFeT),len(nO)])]
lz   = linspace(8.378,8.378+2.131*(len(nFeO)-1),len(nFeO))  # thickness of slab

l = linspace(9,9+((len(nFeO)-1)*2),len(nFeO))

r = array([])
for a,b,c,d in zip(nFeO,nFeT,nO,l):
  # nFeT(II)/nFeT(III)
  y = arange(0,b+1,50)/float(b) 
  # nFeO(II)/nFeO(III)
  x = (-a*q -b*p*y +b*q*y -b*q +c*p) / (a*p - a*q)
  r = append(r,mean((a*x+b*y)/(a*(1.-x)+b*(1.-y))))

# plot data according to eq. in manuscript
axs[0].plot(l,r,label='(001)-SCV',color='C2', linewidth=4)
nfe2_nfe3_dft = array([0,0.055555556,0.136363636,0.233333333,
                       0.264705882,0.30952381])
lz_dft = array([9,13,17,25,29,37])

axs[0].plot(lz_dft,nfe2_nfe3_dft,'x',color='C2', 
            markersize=3, markeredgewidth=12)

axs[0].axhline(0.5,linestyle='--',color='k',
               label=r'Ideal $\mathrm{Fe}_3 \mathrm{O}_4$', 
               linewidth=3)
axs[0].legend(framealpha=0.0, ncol=1, loc='best', fontsize=16)

#################################################


axs[2].plot(df2["layer"], df2["thickness"]/((df2["layer"]+1)/2), 
            "b", linewidth=4, label="(001)-DBT")
axs[2].axhline(y=(25.403165817260742/12), color="black", xmax=1, 
               ls="--", linewidth=3, label="Bulk")

axs[2].legend(framealpha=0.0, ncol=1, loc='best', fontsize=18)
axs[2].set_ylabel(r"$d_\mathrm{oct} \, (\AA)$",labelpad=36, fontsize=24)

axs[2].set_xlim([0, 45])
axs[2].set_xticks([10, 25, 40])

axs[0].text(0.15, 0.85, '(a)',verticalalignment='top', horizontalalignment='right',transform=axs[0].transAxes)
axs[1].text(0.15, 0.85, '(b)',verticalalignment='top', horizontalalignment='right',transform=axs[1].transAxes)
axs[2].text(0.15, 0.85, '(c)',verticalalignment='top', horizontalalignment='right',transform=axs[2].transAxes)

for x in range(3):
    axs[x].grid(color='gray', linestyle='dotted', alpha=0.5, which="minor")
    axs[x].grid(color='gray', linestyle='dotted', alpha=0.5, which="major")


axs[2].set_xlabel("Layer",labelpad=22)
fig.subplots_adjust(hspace=0.1)

fig.savefig('surf_combined.pdf',format='pdf', bbox_inches = "tight")
fig.savefig('surf_combined.png', dpi=300.0,format='png', bbox_inches = "tight")
