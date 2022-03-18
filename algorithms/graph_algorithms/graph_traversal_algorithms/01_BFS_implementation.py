# Breadth First Search implementation

class Node:
    def __init__(self, name):
        self.name = name  # name of a given vertex
        self.adjancency_list = []  # reprsenting the neighbors of the actual node
        self.visited = False  # track whether visited a given node or not

def breadth_first_search(start_node):

    # queue:FIFO -> first inseert first take out
    queue = [start_node]

    # keep iterating (considering all neighbors) until the queue is empty
    while queue:

        # remove and return the first item we inserted
        actual_node = queue.pop(0)
        actual_node.visited = True
        print(actual_node.name)

        # considering all the neighbors to the actual node
        for n in actual_node.adjancency_list:
            if not n.visited:
                queue.append(n)


if __name__ == "__main__":

    # create nodes / verticies
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    # handle the neighbors
    node1.adjancency_list.append(node2)
    node1.adjancency_list.append(node3)
    node2.adjancency_list.append(node4)
    node4.adjancency_list.append(node5)

    # run BFS
    breadth_first_search(node1)

