"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if (v1 or v2) not in self.vertices:
            return "vertex does exist"
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()

        while q.size() > 0:
            current_vertex = q.dequeue()
            if current_vertex not in visited:
                # print(f'vertex: {current_vertex}')
                print(current_vertex)
                visited.add(current_vertex)

                edges = self.get_neighbors(current_vertex)
                for vertex in edges:
                    q.enqueue(vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()

        while stack.size() > 0:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                # print(f'vertex: {current_vertex}')
                print(current_vertex)
                visited.add(current_vertex)

                edges = self.get_neighbors(current_vertex)
                for vertex in edges:
                    stack.push(vertex)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()

        def recursive_print(vertex):
            if vertex not in visited:
                # print(f'vertex: {current_vertex}')
                print(vertex)
                visited.add(vertex)
                edges = self.get_neighbors(vertex)
                for neighbor in edges:
                    recursive_print(neighbor)
            return

        recursive_print(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        path = [starting_vertex]
        q.enqueue(path)
        visited = set()

        while q.size() > 0:
            current_path = q.dequeue()
            vertex = current_path[-1]

            # print('vertex', vertex)
            if vertex not in visited:
                if vertex == destination_vertex:
                    return current_path
                visited.add(vertex)

                edges = self.get_neighbors(vertex)
                for edge in edges:
                    # make a clone, not a reference!!!!
                    new_path = list(current_path)
                    new_path.append(edge)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        path = [starting_vertex]
        stack.push(path)
        visited = set()

        while stack.size() > 0:
            current_path = stack.pop()
            vertex = current_path[-1]

            # print('vertex', vertex)
            if vertex not in visited:
                if vertex == destination_vertex:
                    return current_path
                visited.add(vertex)

                edges = self.get_neighbors(vertex)
                for edge in edges:
                    # make a clone, not a reference!!!!
                    new_path = list(current_path)
                    new_path.append(edge)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # path = [starting_vertex]
        visited = set()

        def recursive_search(path):
            vertex = path[-1]
            # print('vertex', vertex)
            # print('path rcv', path)
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                edges = list(self.get_neighbors(vertex))
                # path.append(edges)
                print('edges', edges)
                for neighbor in edges:
                    new_path = list(path)
                    new_path.append(neighbor)
                    print('list?', new_path)
                    recursive_search(new_path)
            return path

        recursive_search([starting_vertex])


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))
    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
