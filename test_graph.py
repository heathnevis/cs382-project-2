#simple graph testing to verify it worked during early development, not intended as a demo

import main
import random

graph = main.Graph()

for i in range(0,random.randint(1,10)):
    graph.add_vertex(i,
                     random.randint(0,30),
                     random.sample(graph.Vlist,random.randint(0,len(graph.Vlist))),
                     weight=random.randint(1,10))
    
graph.print_graph()