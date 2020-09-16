class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
​
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
​
# LL: network where the nodes can have just one connection
## BST: network where nodes can have a left and a right
​
# Graph
## node aka vertices (one vertex, many vertices)
## connections aka edges
​
# in a graph, we can have a node with no connections
## contrast with LL, where node with no edges isn't in the LL
​
# Network
​
## LL Traversal
## cur = ll.head
## while cur is not None:
### cur = cur.next
​
## BST Traversal
def bst_traversal(node):
    print(node)
    if node == None:
        return
    bst_traversal(node.left)
    bst_traversal(node.right)
​
## Graphs terminology, aka types of graphs
### directed vs undirected
#### one-way street vs two-way streets
#### Twitter: directed, FB/LinkedIn: undirected
​
## acyclic vs cyclic
### 'no circles' vs 'circles'
​
## weighted vs unweighted
### map with distance/traffic
### Use Dijkstra's algorithm
​
### decision graph: weights? cost of purchases, or time
### sparse vs dense graphs
​
## Why traversals are important to other algorithms
## Graph applications
### if you can think of a coding problem as a graph, then you can apply these graph algorithms
​
## things, and connections between them
​
​
class ListNode:
    def __init__(value):
        self.value = value
        self.next = None
a_node = ListNode(1)
b_node = ListNode(2)
a_node.next = b_node
​
​
## basically an adjacency list
class GraphNode:
    def __init__(value):
        self.value = value
        self.neighbors = []
​
node1 = GraphNode(1)
node2 = GraphNode(2)
node3 = GraphNode(3)
node4 = GraphNode(4)
node5 = GraphNode(5)
​
node1.neighbors.append(node2)
node1.neighbors.append(node3)
node1.neighbors.append(node4)
node5.neighbors.append(node4)
node3.neighbors.append(node4)
        
        
        
​
## We also want to generalise traveral!
## Graph traversal will work for LL and BST
### Reps! 
​
​
# depth first or "distant first"
def dft(start_node):
    ## make a stack of nodes to visit
    stack = Stack()
    stack.push(start_node)
​
    ## make a set to track visited nodes
    visited = set()
​
    ## while the stack isn't empty
    while stack.size() > 0:
    ### pop off top of stack, this is our current node
        current_node = stack.pop()
    ### if we have not visited, then let's:
        if current_node not in visited:
    #### mark as visited
            visited.add(current_node)
​
    #### get the vertex's neighbors
            neighbors = current_node.neighbors
    #### put the current node's neighbors on the stack
            for neighbor in neighbors:
                stack.push(neighbor)
​
                
def bft(start_node):
    ## make a queue
    q = Queue()
    ## prime the pump with the first node
    q.enqueue(start_node)
​
    ## make a set to track visited nodes
    visited = set()
​
    ## while the queue isn't empty:
    while q.size() > 0:
    ## dequeue from front of queue, this is our current node
        current_node = q.dequeue()
    ### if we have not visited, let's:
        if current_node not in visited:
    #### mark as visited
            visited.add(current_node)
    #### get the vertex's neighbors
            neighbors = start_node.neighbors
    #### put them in the queue
            for neighbor in neighbors:
                q.enqueue(neighbor)