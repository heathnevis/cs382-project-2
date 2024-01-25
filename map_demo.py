import main

#creates a 5x5 map, with all edge weights being 1, and vertexes
#represented by tuples of their coordinates
m = main.Map(5)

#add_opstacle takes an x and y coordinate (in that order), and makes the vertex on that
#point into an obstacle, meaning all edges to it are set to infinity
m.add_obstacle(2,3)

#remove obstacle does the opposite of add_obstacle, taking the same inputs.
#it resets the edge weights to 1
m.remove_obstacle(2,3)
m.add_obstacle(2,3)

#is_obstacle checks if a coordinate is an obtacle, returning true or false.
print("Is (2,3) an obstacle? ", m.is_obstacle(2,3))


#prints a pretty version of the graph!
#the obstacles are '@', and everything else is an '_'
#remember, indexing starts from 0, so it might look weird
m.print_pretty()

#there are other helper functions, but those are used within larger functions to make them work better
