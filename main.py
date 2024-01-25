import math

# helper function to construct a list object with n items and return it. 
# Helpful for populating new lists
def list_of_length(n):
    ls = []
    i = 0
    while i < n:
        ls.append(None)
        i += 1
    return(ls)

def Merge(A,p,q,r,evaluator):
    n_L = q - p +1 # define the length of the left half
    n_R = r - q # define the length of the right half
    
    # use list_of_length to construct list objects with the proper left and right lengths and store them in L and R
    L = list_of_length(n_L)
    R = list_of_length(n_R)

    # populate Left with the left half of the area to be sorted
    for i in range(0,n_L):
        L[i] = A[p+i]
    
    # populate Right with the right half of the area to be sorted
    for j in range(0,n_R):
        R[j] = A[q+j+1]
    
    # set loop starter variables
    i = 0
    j = 0
    k = p

    # while we have not reached the end of either Left or Right, 
    # swap the lowest element from a comparison of Left and Right back into the main array
    while i < n_L and j < n_R:
        #print(L[i].key)
        if evaluator(L[i]) <= evaluator(R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    # if any of Left remains, put it all in A in order
    while i < n_L:
        A[k] = L[i]
        i += 1
        k += 1
    
    # same as above for Right. Only one of these will execute
    while j < n_R:
        A[k] = R[j]
        j += 1
        k += 1

# use Merge() to recursively divide and conquer until the array is sorted.
# p and r define the start and end indices of the slice of array to be sorted
def Merge_Sort(A,p,r,evaluator):
    if p < r:
        q = math.floor((p+r) / 2)
        Merge_Sort(A,p,q,evaluator)
        Merge_Sort(A,q+1,r,evaluator)
        Merge(A,p,q,r,evaluator)

# user-friendly wrapper of Merge_Sort() that sorts the whole array by default
def Merge_Wrapper(A,evaluator):
    p = 0
    r = len(A) - 1
    Merge_Sort(A,p,r,evaluator)




class Vertex:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.neighbors = []

class Edge:
    def __init__(self, v1,v2, w):
        self.vertices = {v1,v2}
        self.weight = w

class Graph:
    #represents an undirected weighted graph

    def __init__(self):
        #constructs an empty graph object
        self.Vlist = []
        self.Elist = []
        #your code here#
        pass

    def get_weight(self,k_u,k_v):
        #returns the weight of edge between k_u and k_v if it exists (None otherwise)
        for i in self.Elist:
            if (k_u in i.vertices and k_v in i.vertices):
                return i.weight
        return None

    def add_vertex(self,k,v,neighbors=[],weight=1):
        new_vertex = Vertex(k,v)
        self.Vlist.append(new_vertex)
        for connection_target in neighbors:
            self.add_edge(new_vertex,connection_target,weight)
        return new_vertex

    def delete_vertex(self,k):
        #deletes the vertex corresponding to key k from the graph

        #your code here#
        for i in self.Vlist:
            if(i.key == k):
                self.Vlist.remove(i)
        pass

    def add_edge(self,k_u,k_v,w):
        #adds an edge with weight w between the vertices corresponding to keys k_u, k_v (if it doesn't already exist)
        for i in self.Elist:
            if (k_u in i.vertices and k_v in i.vertices and i.weight == w):
                return
        self.Elist.append(Edge(k_u,k_v,w))
        k_u.neighbors.append(k_v)
        k_v.neighbors.append(k_u)


    def delete_edge(self,k_u,k_v):
        #deletes the edge between the vertices corresponding to keys k_u, k_v (if it exists)
        for i in self.Elist:
            if (k_u in i.vertices and k_v in i.vertices):
                self.Elist.remove(i)
        return

    def print_graph(self):
        for vertex in self.Vlist:
            print(str(vertex.key)," (V=",str(vertex.value),")"," -> ",sep="",end="\t")
            print("[",end="")
            for neighbor in vertex.neighbors:
                print(str(neighbor.key),end=",")
            print("]",end="\n")

class Priority_Queue():
    def __init__(self):
        self.items = []
        self.weight_dict = {}
        for x in self.items:
            self.weight_dict[x] = None

    def update_ordering(self):
        def evaluating_function(x):
            return self.weight_dict[x]
        
        Merge_Wrapper(self.items,evaluating_function)

    def push(self,value,weight):
        if weight == None:
            print("!flag!")
        self.items.append(value)
        self.weight_dict[value] = weight
        self.update_ordering()

    def remove(self,value):
        self.items.pop(value)
        self.weight_dict[value] = None
        self.update_ordering()

    def update_weights(self,weight_function):
        for k in self.weight_dict:
            self.weight_dict[k] = weight_function(k)
        self.update_ordering()

    def pop_top(self):
        if len(self.items) > 0:
            return self.items.pop(0)
        else:
            return None
    
    def length(self):
        return len(self.items)
    
    def print_contents(self):
        print(self.items)


class Map(Graph):

    def __init__(self,n,obstacles=[]):
        #creates a map representing the squares of n by n grid
        #optional argument: list of (x,y) locations indicating obstacles (cannot pass through)
        #vertex values: 1 if blocked, 0 if unblocked
        Graph.__init__(self)
        self.n = n

        #loops through n^2 times to make all the vertices, but doesn't add edges
        for i in range(n):
            for j in range(n):
                value = 0
                if ((j,i) in obstacles):
                    value = 1
                self.add_vertex((j,i), value)
        
        for v in self.Vlist:
            new_edges = self.possible_neighbors(v, n)
            for k in new_edges:
                if( v.value == 1): # if there's an obstacle
                    self.add_edge(v, self.retrieve_vertex_from_coordinates(k[0],k[1]), float("inf"))
                else:
                    self.add_edge(v, self.retrieve_vertex_from_coordinates(k[0],k[1]), 1)
        
    def possible_neighbors(self, vertex,n):

        def filter_tester(num):
            return (num in range(n))

        x = vertex.key[0]
        y = vertex.key[1]

        possible_x = [x-1,x+1]
        possible_y = [y-1,y+1]

        possible_x = filter(filter_tester,possible_x)
        possible_y = filter(filter_tester,possible_y)

        possible_coordinates = []
        for x_choice in possible_x:
            possible_coordinates.append((x_choice,y))
        for y_choice in possible_y:
            possible_coordinates.append((x,y_choice))

        return(possible_coordinates)
    
    def print_pretty(self):
        #(optional)
        #prints a pretty ASCII picture of the map using different characters for "open" spaces and obstacles
        #can also show paths, start points, end points, etc
        #your code here#
        i = 0
        while i < self.n:
            j = 0
            while j < self.n:
                if(self.is_obstacle(j,i) == False):
                    print("_",end="")
                else:
                    print("@",end="")
                j += 1  
            print("")
            i += 1
        pass

    def retrieve_vertex_from_coordinates(self,x,y):
        for vertex in self.Vlist:
            if vertex.key[0] == x and vertex.key[1] == y:
                return vertex
            
    def edge_exists(self,v1,v2):
        for edge in self.Elist:
            if v1 in edge.vertices and v2 in edge.vertices and edge.weight != float("inf"):
                return True
        return False
    
    def edge_from_points(self,v1,v2):
        for edge in self.Elist:
            if v1 in edge.vertices and v2 in edge.vertices:
                return edge
        return None

    def add_obstacle(self,x,y):
        blocked_vertex = self.retrieve_vertex_from_coordinates(x,y)
        for curr_neighbor in blocked_vertex.neighbors:
            curr_edge = self.edge_from_points(blocked_vertex,curr_neighbor)
            curr_edge.weight = math.inf
        pass

    def remove_obstacle(self,x,y):
        blocked_vertex = self.retrieve_vertex_from_coordinates(x,y)
        for curr_neighbor in blocked_vertex.neighbors:
            curr_edge = self.edge_from_points(blocked_vertex,curr_neighbor)
            curr_edge.weight = 1
        pass

    def is_obstacle(self,x,y):
        vertex = self.retrieve_vertex_from_coordinates(x,y)
        for neighbor in vertex.neighbors:
            edge = self.edge_from_points(vertex,neighbor)
            if edge.weight != math.inf:
                return False
        return True

    def BFS(self,x,y): #run BFS starting from (x,y)
        vertex = self.retrieve_vertex_from_coordinates(x,y)
        vertex.distance = 0
        vertex.parent = None
        visited = [] #List to store visited nodes
        queue = [] #List for the queue
        visited.append(vertex)
        queue.append(vertex)
        result_dict = {}

        for x in self.Vlist:
            result_dict[x] = {'parent':None,
                              'distance':math.inf}
            x.parent = None
            x.distance = math.inf

        result_dict[vertex] = {
                        'parent':None,
                        'distance':0
                    }
        
        while (len(queue) > 0):
            vertex = queue.pop(0)

            # get the neighbors
            neighborsofvertex = []
            for i in self.Vlist:
                if self.edge_exists(vertex, i):
                    neighborsofvertex.append(i)

            # for each neighbor, if it has not been visited, add to the queue
            for j in neighborsofvertex:
                if j not in visited:
                    visited.append(j)
                    queue.append(j)
                    j.parent = vertex
                    j.distance = j.parent.distance + 1
                    result_dict[j] = {
                        'parent':vertex,
                        'distance':result_dict[vertex]['distance']+1
                    }
        return(result_dict)
    
    def print_all_distances(self,distance_tree):
        i = 0
        while i < self.n:
            j = 0
            while j < self.n:
                if self.is_obstacle(j,i) == False:
                    vertex = self.retrieve_vertex_from_coordinates(j,i)
                    dist = distance_tree[vertex]['distance']
                    if (dist == float("inf")):
                        print("o", end=" ")
                    else:
                        print(dist,end=" ")
                else:
                    print("@",end=" ")
                j += 1  
            print("")
            i += 1

    def BFS_SPSP(self,v1_tuple,v2_tuple):
        vertex = self.retrieve_vertex_from_coordinates(v1_tuple[0],v1_tuple[1])
        end_point = self.retrieve_vertex_from_coordinates(v2_tuple[0],v2_tuple[1])
        if self.is_obstacle(v2_tuple[0],v2_tuple[1]):
            return False
        visited = [] #List to store visited nodes
        queue = [] #List for the queue
        visited.append(vertex)
        queue.append(vertex)
        result_dict = {}

        for x in self.Vlist:
            result_dict[x] = {'parent':None,
                              'distance':math.inf}
            x.parent = None
            x.distance = math.inf
            x.order = math.inf

        vertex.distance = 0
        vertex.parent = None
        vertex.order = 0
        result_dict[vertex] = {
                        'parent':None,
                        'distance':0
                    }
        
        curr_order = 0
        while (len(queue) > 0):
            vertex = queue.pop(0)
            vertex.order = curr_order
            if vertex == end_point:
                return self.nav_through_tree(v1_tuple,v2_tuple,result_dict)

            # get the neighbors
            neighborsofvertex = []
            for i in self.Vlist:
                if self.edge_exists(vertex, i):
                    neighborsofvertex.append(i)

            # for each neighbor, if it has not been visited, add to the queue
            for j in neighborsofvertex:
                if j not in visited:
                    visited.append(j)
                    queue.append(j)
                    j.parent = vertex
                    j.distance = j.parent.distance + 1
                    result_dict[j] = {
                        'parent':vertex,
                        'distance':result_dict[vertex]['distance']+1
                    }
            curr_order += 1
        return self.nav_through_tree(v1_tuple,v2_tuple,result_dict)
    
    #sssp algorithm
    def nav_through_tree(self,source_tuple,target_tuple,paths_tree):
        curr = self.retrieve_vertex_from_coordinates(target_tuple[0],target_tuple[1])
        start = self.retrieve_vertex_from_coordinates(source_tuple[0],source_tuple[1])
        result_path = []
        while curr != start:
            result_path.insert(0,curr)
            curr = paths_tree[curr]['parent']
        result_path.insert(0,curr)
        return(result_path)
    
    def print_single_path_grid(self,v1_tuple,v2_tuple,path):
        i = 0
        while i < self.n:
            j = 0
            while j < self.n:
                if self.is_obstacle(j,i) == False:
                    vertex = self.retrieve_vertex_from_coordinates(j,i)
                    if vertex in path:
                        print(path.index(vertex),end="")
                    else:
                        print("_",end="")
                else:
                    print("@",end="")
                j += 1  
            print("")
            i += 1

    def Dijkstra(self,x,y): #run Dijkstra starting from (x,y)
        vertex = self.retrieve_vertex_from_coordinates(x,y)
        vertex.distance = 0
        vertex.parent = None
        vertex.order = 0
        visited = [] #List to store visited nodes
        queue = Priority_Queue()
        visited.append(vertex)
        queue.push(vertex,0)
        result_dict = {}

        for x in self.Vlist:
            result_dict[x] = {'parent':None,
                              'distance':math.inf}
            x.parent = None
            x.distance = math.inf
            x.order = math.inf

        result_dict[vertex] = {
                        'parent':None,
                        'distance':0
                    }
        
        curr_order = 0
        while (queue.length() > 0):
            vertex = queue.pop_top()
            vertex.order = curr_order

            # get the neighbors
            neighborsofvertex = []
            for i in self.Vlist:
                if self.edge_exists(vertex, i):
                    neighborsofvertex.append(i)

            # for each neighbor, if it has not been visited, add to the queue
            for j in neighborsofvertex:
                if j not in visited:
                    j.parent = vertex
                    j.distance = j.parent.distance + 1
                    visited.append(j)
                    queue.push(j,j.distance)
                    
                    result_dict[j] = {
                        'parent':vertex,
                        'distance':result_dict[vertex]['distance']+1
                    }
            curr_order += 1
        return(result_dict)
    
    def Dijkstra_SPSP(self,tuple_1,tuple_2): #run BFS starting from (x,y)
        vertex = self.retrieve_vertex_from_coordinates(tuple_1[0],tuple_1[1])
        target = self.retrieve_vertex_from_coordinates(tuple_2[0],tuple_2[1])
        if self.is_obstacle(tuple_2[0],tuple_2[1]):
            return False
        visited = [] #List to store visited nodes
        queue = Priority_Queue()
        visited.append(vertex)
        result_dict = {}

        for x in self.Vlist:
            result_dict[x] = {'parent':None,
                              'distance':math.inf}
            x.parent = None
            x.distance = math.inf
            x.order = math.inf

        vertex.distance = 0
        vertex.parent = None
        vertex.order = 0
        queue.push(vertex,0)

        result_dict[vertex] = {
                        'parent':None,
                        'distance':0
                    }
        
        curr_order = 0
        while (queue.length() > 0):
            vertex = queue.pop_top()
            vertex.order = curr_order
            if vertex == target:
                return self.nav_through_tree(tuple_1,tuple_2,result_dict)

            # get the neighbors
            neighborsofvertex = []
            for i in self.Vlist:
                if self.edge_exists(vertex, i):
                    neighborsofvertex.append(i)

            # for each neighbor, if it has not been visited, add to the queue
            for j in neighborsofvertex:
                if j not in visited:
                    j.parent = vertex
                    j.distance = j.parent.distance + 1
                    visited.append(j)
                    queue.push(j,j.distance)
                    result_dict[j] = {
                        'parent':vertex,
                        'distance':result_dict[vertex]['distance']+1
                    }
            curr_order += 1
        return self.nav_through_tree(tuple_1,tuple_2,result_dict)

    def h1(self, vertex):
        weight = math.sin(vertex.distance) 
        return weight
    
    def WhateverFirstSearch(self, source_tuple, h):
        queue = Priority_Queue()
        visited = [] #List to store visited nodes
        vertex = self.retrieve_vertex_from_coordinates(source_tuple[0],source_tuple[1])  
        
        visited.append(vertex)
        
        result_dict = {}
        for x in self.Vlist:
            result_dict[x] = {'parent':None,
                              'distance':math.inf}
            x.parent = None
            x.distance = math.inf
        vertex.distance = 0
        vertex.parent = None
        queue.push(vertex,h(vertex))
        result_dict[vertex] = {
                        'parent':None,
                        'distance':0
                    }
        while (queue.length() > 0):
            vertex = queue.pop_top()
            # get the neighbors
            neighborsofvertex = []
            for i in self.Vlist:
                if self.edge_exists(vertex, i):
                    neighborsofvertex.append(i)

            # for each neighbor, if it has not been visited, add to the queue
            for j in neighborsofvertex:
                if j not in visited:
                    visited.append(j)
                    j.parent = vertex
                    j.distance = j.parent.distance + 1
                    result_dict[j] = {
                        'parent':vertex,
                        'distance':result_dict[vertex]['distance']+1
                    }
                    queue.push(j,h(j))
        return(result_dict)


    
    def print_dijkstra(self,x,y):
        self.print_all_distances(self.Dijkstra(x,y))
    
    def print_BFS(self,x,y):
        self.print_all_distances(self.BFS(x,y))

    def print_dijkstra_SPSP(self,source,target):
        path = self.Dijkstra_SPSP(source, target)
        self.print_single_path_grid(source,target,path)

    def print_BFS_SPSP(self,source,target):
        path = self.BFS_SPSP(source, target)
        self.print_single_path_grid(source,target,path)

    def print_hit_order(self,source,target,spsp_method):
        if spsp_method(source,target):
            print("*" * 10)
            print("Dimensions of map:\t",self.n,"x",self.n,sep="")
            print("Source Coordinates: ",self.retrieve_vertex_from_coordinates(source[0],source[1]).key)
            print("Target Coordinates: ",self.retrieve_vertex_from_coordinates(target[0],target[1]).key)
            vertices_visited = 0
            for i in range(self.n):
                for j in range(self.n):
                    vertex = self.retrieve_vertex_from_coordinates(j,i)
                    if vertex.order != math.inf:
                        vertices_visited += 1
                        if self.is_obstacle(j,i) == False:
                            if [j,i] == source or [j,i] == target:
                                print("\033[1m",vertex.order,"\033[0m",sep="",end="\t")
                            else:
                                print(vertex.order,end="\t")
                        else:
                            print("@",vertex.order,"@",sep="",end="\t")
                    else:
                        print("o",end="\t")
                    j += 1  
                print("\n")
            print("Total vertices visited: ",vertices_visited)
            print("*" * 10)
        else:
            print("*" * 10)
            print("Navigation not possible, target is obstacle.")
            print("*" * 10)

    def print_WFS(self,source,h):
        self.print_all_distances(self.WhateverFirstSearch(source,h))



