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


class Graph:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room_id):
        if room_id not in self.rooms:
            self.rooms[room_id] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}

    def add_connection(self, r1, r2, direction):
        r1_id = r1.id
        r2_id = r2.id

        if r1_id in self.rooms and r2_id in self.rooms:
            self.rooms[r1_id][direction] = r2
        else:
            raise IndexError('That vertex does not exist!')
