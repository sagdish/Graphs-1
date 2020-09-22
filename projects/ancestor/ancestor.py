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


def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    q.enqueue(starting_node)

    while q.size() > 0:
        currentNode = q.dequeue()
        parent = -1
        parent2 = -1
        gen = 0

        for pair in ancestors:
            if (currentNode == pair[1]):
                parent = pair[0]

    return parent


earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8),
                   (8, 9), (11, 8), (10, 1)], 6)
