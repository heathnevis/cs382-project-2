import main

graph2 = main.Graph()

for i in range(2):
            for j in range(2):
                #adding a vertex requires a key (which is a tuple in this case), and a value (i+j in this case).
                #you have to option to specify neighbors as the 3rd argument, which will add edges between the
                #new vertex and the listed neighbors. You can also add a weight, which defaults to 1
                graph2.add_vertex((i,j), i+j)

#adding edges just requires the two vertices the edge goes between, and the weight of the edge.
#if the edge already exists, then it will not do anything
graph2.add_edge(graph2.Vlist[0], graph2.Vlist[1], 1)
graph2.add_edge(graph2.Vlist[3], graph2.Vlist[1], 1)
graph2.add_edge(graph2.Vlist[1], graph2.Vlist[2], 1)

#deleting a vertex requires just the key of the vertex to be deleted.
#if it doesn't exist, it does nothing
graph2.delete_vertex(graph2.Vlist[0])
#deleting an edge is similar to deleting a vertex, but you provide the two vertices,
#and it deletes the edge from both vertices' lists
graph2.delete_edge(graph2.Vlist[3], graph2.Vlist[1])
graph2.delete_edge(graph2.Vlist[3], graph2.Vlist[1])

#getting the weight of an edge takes two vertices and returns the weight of the edge between them,
#returning 'none' if there is no edge
print("weight of edge:", graph2.get_weight(graph2.Vlist[1], graph2.Vlist[2]))

#printing will print out the key and value for each vertex, as well as a list of the neightbors
graph2.print_graph()
