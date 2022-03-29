def traversal(start_vertex, graph):

    #This unified algorithm takes a graph, a start_vertex part of this graph, 
    #and performs graph traversal using a queuing structure. 
    #The algorithm returns the list of explored_vertices, and a 
    #routing table to navigate the graph. 

    # First we create either a LIFO a FIFO
    queuing_structure = new_queuing_structure() 