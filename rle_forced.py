# Check whether an rle pattern contains a self-forcing patch

from pattern_basics import degollify, mat_to_pattern, print_pattern
from gol_agars import find_self_forcing

rle = """
x = 21, y = 18, rule = B3/S23
4b2o3b2o2bo2b2o$2obobo3bo2bobo2bo$ob2obob2o2b2o2b2o$5b2o2b2o2b2o2b3o$b
2obo3bo3bo3bo2bo$obob3ob3ob3ob3o$o2bo3bo3bo3bo$b2o2b2o2b2o2b2o2b2o$3b
2o2b2o2b2o2b2o2bo$b2o2b2o2b2o2b2o2b2o$o3bo3bo3bo3bo$3ob3ob3ob3ob5o$3bo
3bo3bo3bo4bo$2bo2b2o2b2o2b2o2b2o$2b3o2b2o2b2o2b2ob2o$5b2o2bo2bobo$4bo
2b2o3bobo$4b2o7bo!
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

pat = mat_to_pattern(degollify(rle))
print("Input pattern")
print_pattern(pat)
print("Finding maximal self-forcing patch")
print_pattern(find_self_forcing(pat, temp, shift=shift, instance=instance))
