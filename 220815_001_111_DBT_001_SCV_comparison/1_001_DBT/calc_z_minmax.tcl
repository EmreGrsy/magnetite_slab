package require topotools
package require pbctools

set file [open "minmax_z.data" w]

for {set l 15} {$l <= 47} {incr l 2} {

	topo readlammpsdata 001-dbt_3x3_${l}L.data

	set slab [atomselect top all]
	set zlo [expr [lindex [measure minmax $slab] 0 2]-12]
	set zhi [expr [lindex [measure minmax $slab] 1 2]+12]
	
	puts $file "$l [format "%.4f %.4f" $zlo $zhi] zlo zhi"

	unset slab
	unset zlo
	unset zhi

	clear
}

close $file
