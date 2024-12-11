package require topotools
package require pbctools

topo readlammpsdata 001-scv_3x3_53L_init.data

set bottom [atomselect top "all and z<17"]
set top [atomselect top "all and z>42"]

set type4 [atomselect top "all and 42.5>=z and z>=17"]

$type4 set type 4

topo writelammpsdata a-001-scv-53.data full
