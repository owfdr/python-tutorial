from icecream import ic
from termcolor import colored

print("---------- compound")
ic([1, 2, 3])
ic([1, "2", 3.0])

print("---------- indexed")
ic([1, 2, 3][0])
ic([1, 2, 3][-1])

print("---------- sliced")
ic([1, 2, 3][0:2])
ic([1, 2, 3][-2:])
ic([1, 2, 3][:], "(shallow copy)")

print("---------- operations")
list = [1, 2]
ic(list)
ic(list + [3], list)
list[0:2] = ["A", "B"]
ic('list[0:3] = ["A", "B", "C]', list)
list[:] = []
ic("list[:] = []", list)

print("---------- methods")
ic(list)
ic(list.append(3), list)
ic(list.append(2**2), list)

print("---------- built-in function")
ic(list)
ic(len(list))

print("---------- nested")
ic([1, 2, [3, [4]]])
ic([1, 2, [3, [4]]][2][1][0])
