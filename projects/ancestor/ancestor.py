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
    parents = []

    while q.size() > 0:
        currentNode = q.dequeue()
        gen = 0

        for pair in ancestors:
            if (currentNode == pair[1]):
                gen += 1
                print('reached')
                if gen > 1:
                    if parents[-1] < pair[0]:
                        temp = parents[-1]
                        parents[-1] = pair[0]
                        parents.append(temp)
                        continue
                parents.append(pair[0])
                print(parents)
                q.enqueue(pair[0])

    return parents[-1] if len(parents) > 0 else -1


print(
    earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8),
                       (8, 9), (11, 8), (10, 1)], 1))
