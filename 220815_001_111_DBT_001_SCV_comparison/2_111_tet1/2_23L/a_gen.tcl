package require topotools
package require pbctools

topo readlammpsdata m111-tet.data

set bottom [atomselect top "all and z<10.9"]
set top [atomselect top "all and z>54"]

set type4 [atomselect top "all and 54>=z and z>=10.9"]

$type4 set type 4

topo writelammpsdata a-m111-tet.data full
