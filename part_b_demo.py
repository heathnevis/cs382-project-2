import main

#first, we need to construct a map to run the new code on
m = main.Map(5)
m.add_obstacle(0,3)
m.add_obstacle(1,3)

#the following code runs BFS-SSSP on (1,1)
result = m.BFS(1,1)

#the m.BFS(1,1) performes BFS-SSSP using the point (1,1) as the source
#this displays the output of BFS-SSSP starting at (1,1)
print("BFS-SSSP(1,1)")
m.print_all_distances(m.BFS(1,1))

#this does the same, but using a wrapper function to make it nicer
#it also uses a different point as the source (0,4)
print("\nBFS(0,4)")
m.print_BFS(0,4)


#the following code runs BFS-SPSP from (1,1) to (0,4)
path = m.BFS_SPSP([1,1], [0,4])

#this prints out the result from above
print("\nBFS-SPSP([1,1],[0,4])")
m.print_single_path_grid([1,1],[0,4],path)

#we can also use the following code, which uses a wrapper function
#to make it simpler to use. It only requires the source and target,
#but runs the same code
print("\nBFS-SPSP([1,1], [0,4])")
m.print_BFS_SPSP([1,1], [0,4])


