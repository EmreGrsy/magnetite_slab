# In 3x3x3 001-DBT surfaces, each oct layer has 36 fe_oct ions.

package require topotools
package require pbctools

set fe3oct_ratio {}

set nlayer 41
topo readlammpsdata 111-tet1-41L_swp.data

# Topmost ions zmin and zmax
set tet1 {64.4 64.7}
set oct1 {62.3 63.3}
set tet2 {60.7 61.3}
set oct2 {59.925 60.625}

set dtet1 4.80207
set doct1 4.90464
set dtet2 4.85703
set doct2 4.799274

# Zmin and zmax of each layer
set tet1_zlayer {}
set oct1_zlayer {}
set tet2_zlayer {}
set oct2_zlayer {}

# random layer thickness
set layer 8

## tet1
for {set x 0} {$x < $layer} {incr x} {

	set zmin [expr {[lindex $tet1 0] - $x*$dtet1}]
	set zmax [expr {[lindex $tet1 1] - $x*$dtet1}]

	lappend tet1_zlayer [list $zmin $zmax]
}

## oct1
for {set x 0} {$x < $layer} {incr x} {

        set zmin [expr {[lindex $oct1 0] - $x*$doct1}]
        set zmax [expr {[lindex $oct1 1] - $x*$doct1}]

        lappend oct1_zlayer [list $zmin $zmax]
}

## tet2
for {set x 0} {$x < $layer} {incr x} {

        set zmin [expr {[lindex $tet2 0] - $x*$dtet2}]
        set zmax [expr {[lindex $tet2 1] - $x*$dtet2}]

        lappend tet2_zlayer [list $zmin $zmax]
}

## oct2
for {set x 0} {$x < $layer} {incr x} {

        set zmin [expr {[lindex $oct2 0] - $x*$doct2}]
        set zmax [expr {[lindex $oct2 1] - $x*$doct2}]

        lappend oct2_zlayer [list $zmin $zmax]
}


for {set x 0} {$x < $layer} {incr x} {

        set nT1fe3 [atomselect top "type 2 and z>[lindex $tet1_zlayer $x 0] and z<[lindex $tet1_zlayer $x 1]"]
        set nT1fe2 [atomselect top "type 1 and z>[lindex $tet1_zlayer $x 0] and z<[lindex $tet1_zlayer $x 1]"]

        set nO1fe3 [atomselect top "type 2 and z>[lindex $oct1_zlayer $x 0] and z<[lindex $oct1_zlayer $x 1]"]
        set nO1fe2 [atomselect top "type 1 and z>[lindex $oct1_zlayer $x 0] and z<[lindex $oct1_zlayer $x 1]"]

	set nT2fe3 [atomselect top "type 2 and z>[lindex $tet2_zlayer $x 0] and z<[lindex $tet2_zlayer $x 1]"]
	set nT2fe2 [atomselect top "type 1 and z>[lindex $tet2_zlayer $x 0] and z<[lindex $tet2_zlayer $x 1]"]
    
    	set nO2fe3 [atomselect top "type 2 and z>[lindex $oct2_zlayer $x 0] and z<[lindex $oct2_zlayer $x 1]"]
        set nO2fe2 [atomselect top "type 1 and z>[lindex $oct2_zlayer $x 0] and z<[lindex $oct2_zlayer $x 1]"]

	puts "[$nT1fe3 num] [$nT1fe2 num] - [$nO1fe3 num] [$nO1fe2 num] - [$nT2fe3 num] [$nT2fe2 num] - [$nO2fe3 num] [$nO2fe2 num]"

}
