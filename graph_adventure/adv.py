from room import Room
from player import Player
from world import World
from util import Stack, Queue, Graph
from graphs.graph_1 import roomGraph_1

import random

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.


world.loadGraph(roomGraph)
world.printRooms()
player = Player("Name", world.startingRoom)


"""
TASK: 
You are responsible for filling traversalPath with directions that, when walked in order, will visit every room on the map at least once.

 Need to construct my own traversal graph.
 Room 0 starts with the exits [n, s, w, e]

 Starting graph should look like this:
 {
   0: {'n': ?, 's': ?, 'w': ?, 'e': ?}
 }

"""


# traversal_graph = Graph()
# print(world.startingRoom.getRoomInDirection('n'))

traversalPath = ['n', 's']


def flip(d):
    if d == 'n':
        return 's'
    elif d == 's':
        return 'n'
    elif d == 'w':
        return 'e'
    elif d == 'e':
        return 'w'


# def bft(starting_room):
#     qq = Queue()
#     visited = set()

#     qq.enqueue(starting_room)

#     while qq.size() > 0:
#         current_room = qq.dequeue()

#         if current_room.id not in visited:
#             visited[current_room.id] = current_room.getExits()

#             for direction in current_room.getExits():
#                 qq.enqueue(current_room.getRoomInDirection(direction))

#     return visited


# def get_directions(graph):
#     test_player = Player('Name', world.startingRoom)
#     for i in graph:
#         # print(i)
#         for j in graph[i]:
#             traversalPath.append(j)


# def bft(starting_room):
#     qq = Queue()
#     visited = {}
#     # traversal_graph = Graph()

#     qq.enqueue([starting_room])

#     while qq.size() > 0:
#         path = qq.dequeue()
#         current_room = path[-1]

#         if current_room.id not in visited:
#             # traversal_graph.add_room(current_room.id)

#             visited[current_room.id] = current_room.getExits()
#             # print(current_room.id, current_room.getExits())

#             for direction in current_room.getExits():
#                 # if traversal_graph.rooms[current_room.id][direction] == '?':
#                 #     pass
#                 # traversalPath.append(direction)
#                 # qq.enqueue(current_room.getRoomInDirection(direction))
#                 path_copy = list(path)
#                 path_copy.append(current_room.getRoomInDirection(direction))
#                 qq.enqueue(path_copy)

#     return [room.id for room in path]


# def dft(starting_room):
#     stack = Stack()
#     # traversal_graph = Graph()
#     visited = {}
#     stack.push(starting_room)
#     test_player = Player("Name", starting_room)

#     while stack.size() > 0:
#         current_room = stack.pop()

#         if current_room.id not in visited:
#             visited[current_room.id] = current_room.getExits()

#             for direction in current_room.getExits():

#                 stack.push(current_room.getRoomInDirection(direction))

#     return visited
    #     if current_room.id not in traversal_graph.rooms:
    #         traversal_graph.add_room(current_room.id)

    #         for direction in traversal_graph.rooms[current_room.id]:
    #             if direction == '?':
    #                 if current_room.getRoomInDirection(direction) is not None:
    #                     next_room = current_room.getRoomInDirection(direction)
    #                     player.travel(direction)
    #                     traversalPath.append(direction)

    #                     traversal_graph.add_room(next_room.id)
    #                     traversal_graph.add_connection(
    #                         current_room, next_room, direction)

    #                     stack.push(next_room)

    # return traversal_graph.rooms
# print(bft(world.startingRoom))

# # print('\n---dft----\n')

# # print(dft(world.startingRoom))

# print('\n-------\n')

# print(get_directions(bft(world.startingRoom)))

# print('\n----traversalPath---\n')

# print(traversalPath)

# print(traversalPath)

# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)
for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == len(roomGraph):
    print(
        f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")
