import main

#first, we need to construct a map to run the new code on
m = main.Map(5)
m.add_obstacle(3,3)
m.add_obstacle(2,3)
m.add_obstacle(1,3)

#we can use Dijkstra to find the shortest paths to
#each point aside from the source
sssp = m.Dijkstra(1,1)


#we can visualize the result using
print("dijkstra SSSP (1,1)")
m.print_dijkstra(1,1)
#or we can use
print("dikstra SSSP(1,1)")
m.print_all_distances(sssp)
