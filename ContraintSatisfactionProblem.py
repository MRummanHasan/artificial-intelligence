# this logic needs serious improvements
#
# Project : Constraint Satisfaction Problem
# Author : Rumman
# Date : 15-11-2018
# Problem : Map Coloring Problem
# Dependency : Python 3
#

# Variable = var_region are the abbr for name of territories in Australia
var_region = ["WA", "NSW", "SA", "NT", "Q", "V"]
# No consective regions_wrt_neighbour can have saem color
constraint_val = 2
# Domain = we have 3 different color
domain = ['R', 'G', 'B']

regions_wrt_neighbour = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "NSW": ["Q", "SA", "V"],
    "Q": ["NT", "SA", "NSW"],
    "V": ["NSW", "SA"]
}

####### ------ SOLUTION ------ #######

# Input: All regions, Constraint count, Region w.r.t neighbour
# Problem: Since there are 3 domain values(i.e: r,g,b) therefore no regions shall has 3 neighbour
# Output: True / False


def check_no_of_neighbour(var_region, constraint_val, regions_wrt_neighbour):
    for r in var_region:
        print(r, "has", len(
            regions_wrt_neighbour[r]), "neighbours. Which are:", regions_wrt_neighbour[r])

        if len(regions_wrt_neighbour[r]) > constraint_val:
            print("\nConstraint not Satisfied at", r)
            return False

    print("This map will satisfy contraint")
    return True




check = check_no_of_neighbour(var_region, constraint_val, regions_wrt_neighbour)
print(check)
