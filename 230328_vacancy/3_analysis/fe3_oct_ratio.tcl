# In 3x3x3 001-DBT surfaces, each oct layer has 36 fe_oct ions.

package require topotools
package require pbctools

set fe3oct_ratio {}

set nlayer 21
set over_head 001-dbt_3x3_21L

# Number of oct layers
set noctl [expr {($nlayer +1)/2}]

# Topmost fe_oct ions zmin and zmax
set topmost {21 22}

# Distance between fe oct layers
set oct_oct 2.1

set info_data [open "info1.data" r]

set log [open "${nlayer}L_info2.data" w]

while {[gets ${info_data} line] != -1} {
	
	set step [lindex [split $line "_*K.data"] 0]
	set mc_temp [lindex [split $line "_*K.data"] 1]

        puts "${step}_${mc_temp}K"	
	topo readlammpsdata ${over_head}_${line}

	set dummy_ratio {}
	
	# Zmin and zmax of each fe_oct layer
	set zlayer {}

	lappend dummy_ratio $mc_temp

	# Sanity check
	#puts "$step $mc_temp"

	for {set x 0} {$x < $noctl} {incr x} {

        	set zmin [expr {[lindex $topmost 0] - $x*$oct_oct}]
        	set zmax [expr {[lindex $topmost 1] - $x*$oct_oct}]

        	lappend zlayer [list $zmin $zmax]
	}

	# Count fe_oct ion of each oct layer
	for {set x 0} {$x < $noctl} {incr x} {

        	#set oct3 [atomselect top "type 2 and z>[lindex $zlayer $x 0] and z<[lindex $zlayer $x 1]"]
        	set oct2 [atomselect top "type 4 and z>[lindex $zlayer $x 0] and z<[lindex $zlayer $x 1]"]

        	set toct [expr [$oct2 num]]

        	if {$toct!=36} {
                	puts "ERROR: missing fe_oct ion at [expr {$x+1}] layer"
        	}

		# Sanity check
        	#puts "[expr {$x+1}] [$oct3 num]"

        	lappend dummy_ratio [$oct2 num]

		# Cleanup
###		$oct3 delete
		$oct2 delete
	}

	lappend fe3oct_ratio $dummy_ratio
	#puts "$fe3oct_ratio"
}

foreach temp_ratio $fe3oct_ratio {
	puts $log "$temp_ratio"
}

exit
