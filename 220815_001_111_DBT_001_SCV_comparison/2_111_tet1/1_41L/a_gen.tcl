package require topotools
package require pbctools

topo readlammpsdata m111-tet.data

set bottom [atomselect top "all and z<18"]
set top [atomselect top "all and z>47"]

set type4 [atomselect top "all and 47>=z and z>=18"]

$type4 set type 4

topo writelammpsdata a-m111-tet.data full
