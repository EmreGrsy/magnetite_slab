# change background color to green for better post-processing
color Display Background white
display Backgroundgradient off
axes location off

package require topotools
package require pbctools

set nlayer 25

topo readlammpsdata 001-dbt_3x3_${nlayer}L_swp.data

topo guessatom lammps data

## Define Fe_tet ions

# Number of tet layers
set noctl [expr {($nlayer +1)/2}]

# Topmost fe_oct ions zmin and zmax
set topmost {15.2 16.2}

# Distance between fe oct layers
set oct_oct 2.1

# Initialize zlayer
set zlayer {} 

for {set x 0} {$x < $noctl} {incr x} {
	
	set zmin [expr {[lindex $topmost 0] - $x*$oct_oct}]
	set zmax [expr {[lindex $topmost 1] - $x*$oct_oct}]

	lappend zlayer [list $zmin $zmax]
}	 

# Count fe ions within each oct layer
for {set x 0} {$x < $noctl} {incr x} {

	set tet_3 [atomselect top "type 7 and z>[lindex $zlayer $x 0] and z<[lindex $zlayer $x 1]"]
	set tet_2 [atomselect top "type 6 and z>[lindex $zlayer $x 0] and z<[lindex $zlayer $x 1]"]
	
	$tet_3 set type 1
	$tet_2 set type 2

}

## Visualization and rendering

# Explicitly define Carbon's color
color add item Type 1 purple
color Type 1 purple

display resetview

# Rotate for better visuals
rotate x by -90
rotate y by 45
#rotate x by 2
#rotate y by 2

# Delete default representation
mol delrep 0 top

# Cartoon display
material add Cartoon
material change ambient Cartoon 0.00
material change diffuse Cartoon 0.90
material change specular Cartoon 0.00
material change shininess Cartoon 0.00
material change mirror Cartoon 0.00
material change opacity Cartoon 1.00
material change outline Cartoon 4.00
material change outlinewidth Cartoon 0.35

# Trans1 display
material add Trans1
material change ambient Trans1 0.00
material change diffuse Trans1 0.90
material change specular Trans1 0.00
material change shininess Trans1 0.00
material change mirror Trans1 0.00
material change opacity Trans1 0.40
material change outline Trans1 4.0
material change outlinewidth Trans1 0.35

# Fe2_oct ions
mol representation vdw 0.5 1000
mol color charge
mol material Cartoon
mol selection {type 6}
mol addrep top

# Fe3_oct ions
mol representation vdw 0.5 1000
mol color charge
mol material Cartoon
mol selection {type 7}
mol addrep top

# Fe_tet ions
#mol representation vdw 0.4 1000
#mol color type
#mol material Cartoon
#mol selection {type 1}
#mol addrep top

## All
#mol representation vdw 0.4 1000
#mol color charge
#mol material Cartoon
#mol selection {all and not type 1 and type 7}
#mol addrep top


# Fe_tet ions
#mol representation vdw 0.5 1000
#mol color type
#mol material Trans1
#mol selection {type 1}
#mol addrep top

#  Oxygen
#mol representation vdw 0.5 1000
#mol color charge
#mol material Trans1
#mol selection {type 8}
#mol addrep top


# Formate
#mol representation vdw 0.5 1000
#mol color Name
#mol material Cartoon
#mol selection {same fragment as index 488}
#mol addrep top

# Surface hydroxyl
#mol representation vdw 0.5 1000
#mol color Name
#mol material Cartoon
#mol selection {index 978 757}
#mol addrep top

# Center the system
#set sys [atomselect top all]
# Original displacment 0 0 -15
#$sys moveby {0 0 -15}

# Display settings
display depthcue off
display cuemode Exp2
display cuestart 0.50
display cueend 10.00
display cuedensity 0.32
display eyesep 0.07
display focalLength 2.00
display height 4.0
display distance -2.00
display culling off
display fps off
display stereoswap off
display cachemode Off
display projection Orthographic
display shadows on
display ambientocclusion on
display aoambient 0.80
display aodirect 0.40

display update

# Rendering options
# --asamples 24 -res 7680 4800  
render Tachyon ${nlayer}_oct_only "/usr/local/lib/vmd/tachyon_LINUXAMD64" -fullshade -trans_vmd -aasamples 12 %s -format TARGA -res 768 480 -o %s.tga

