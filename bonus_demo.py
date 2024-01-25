import math
import main

m = main.Map(5)
m.add_obstacle(3,3)
m.add_obstacle(2,3)
m.add_obstacle(1,3)

#we can run WFS by selecting a starting point ([0,0] in this case), 
# and a heuristic function (h1, which assigns weight to be sin(distance))
result = m.WhateverFirstSearch([0,0],m.h1)

#we can print the result from WFS using the print_all_distances function
print("WFS([0,0], m.h1)")
m.print_all_distances(result)

#we can also combine the two functions with the wrapper function
#which simplifies it a bit
print("\nWFS([0,0], m.h1)")
m.print_WFS([0,0],m.h1)


#for Dijkstra, we added a SPSP function, which will make it
#exit early when it reaches the goal tile
#we can see the order that tiles are visited with the following code:
m.print_hit_order([0,0],[2,2], m.Dijkstra_SPSP)
#this takes in the source point, the target point, and the pathfinding method


map1 = main.Map(5)
map1.add_obstacle(2,3)
map1.add_obstacle(1,2)
map1.add_obstacle(4,4)

map2 = main.Map(6)
map2.add_obstacle(3,3)
map2.add_obstacle(1,1)
map2.add_obstacle(4,4)

map1.print_hit_order([0,0],[3,3],map1.Dijkstra_SPSP)
map1.print_hit_order([0,0],[3,3],map1.BFS_SPSP)

map2.print_hit_order([3,2],[4,5],map2.Dijkstra_SPSP)
map2.print_hit_order([3,2],[4,5],map2.BFS_SPSP)

print("In all maps we have tested, the number of vertices visited by single source Dijkstra and single source BFS are the same. This is likely because our maps are unweighted, so Djikstra's sorting function essentially has no effect, since all distance estimates are the same. Were our maps directly weighted, we might observe a different result wherein Dijkstra would visit fewer nodes before reaching the goal.")
