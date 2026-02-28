# Check whether an rle pattern contains a self-forcing patch

from pattern_basics import degollify, mat_to_pattern, print_pattern
from gol_agars import find_self_forcing

rle = """
x = 39, y = 39, rule = B3/S23
9b2ob2o11b2ob2o$7bo2bobo2b2o5b2o2bobo2bo$2ob2o2b2o2bo2b2obo3bob2o2bo2b
2o2b2ob2o$o3b3o10bo3bo10b3o3bo$b2o4b6ob3o5b3ob6o4b2o$2b2ob3o4b3o9b3o4b
3ob2o$2bo2bo5bo15bo5bo2bo$b2o3b3obo2b4o2bo2b4o2bob3o3b2o$o2b3obob2o2bo
2b7o2bo2b2obob3o2bo$obo3bo2bo19bo2bo3bobo$bobo5b21o5bobo$3bo2b3o4bo5bo
5bo4b3o2bo$3bob2obo3bobo3bobo3bobo3bob2obo$b2o4bobob5ob5ob5obobo4b2o$o
2b4obobo5bo5bo5bobob4o2bo$bo7bobo3bobo3bobo3bobo7bo$2obo2bobob3ob5ob5o
b3obobo2bob2o$2b2obobobo3bo5bo5bo3bobobob2o$2bo2b2obo3bobo3bobo3bobo3b
ob2o2bo$b2o2bob2o2b5ob5ob5o2b2obo2b2o$bo4bo2b2o5bo5bo5b2o2bo4bo$3bo5bo
bo3bobo3bobo3bobo5bo$2b2o2bobob3ob5ob5ob3obobo2b2o$6b2obo3bo5bo5bo3bob
2o$4o3b2o3bobo3bobo3bobo3b2o3b4o$o2bob2ob2ob5ob5ob5ob2ob2obo2bo$5bo10b
o5bo10bo$5b2o2b3o3bobo3bobo3b3o2b2o$3b2obo2bob2ob5ob5ob2obo2bob2o$3bo
2bo2bo2bo6bo6bo2bo2bo2bo$5bob3o2b3o3bobo3b3o2b3obo$6b2ob2obob2ob5ob2ob
ob2ob2o$15bo7bo$2bob3o2b4obob2o3b2obob4o2b3obo$2b2obo2bo3b2obob2ob2obo
b2o3bo2bob2o$7b2ob2o3bo7bo3b2ob2o$8bob2o3bob2ob2obo3b2obo$6bo9bobobobo
9bo$6b2o23b2o!
"""

# We find and print the largest subpattern that forces itself in all nth preimages, shifted by -shift.
# "No pattern" means the input is an (nth generation) orphan.
# "Empty pattern" means the pattern contains no self-forcing patch with these parameters.
# Note: even though there is no self-forcing patch with n and shift,
# there might be one with k*n and k*shift for some k >= 2.

# Number of iterations n
temp = 2
# Spatial shift
shift = (0,0)
# SAT instance construction method
instance = "sort_network"
#instance = "bisector"

rule = ([3], [2,3])

pat = mat_to_pattern(degollify(rle))
print("Input pattern")
print_pattern(pat)
print("Finding maximal self-forcing patch")
print_pattern(find_self_forcing(pat, temp, shift=shift, instance=instance, rule=rule))
