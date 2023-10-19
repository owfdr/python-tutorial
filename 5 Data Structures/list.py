from icecream import ic

list = []

ic(list)

ic(list.append(1), list)

ic(list.extend((2, 3)), list)

ic(list.insert(0, 0), list)

ic(list.remove(3), list)

ic(list.pop(), list)

ic(list.pop(0), list)

ic(list.clear(), list)

print("----------")

list = [3, 2, 1]

ic(list)

ic(list.index(1), list)

ic(list.count(1), list)

ic(list.sort(), list)

ic(list.reverse(), list)

ic(list.copy())

# Will not work.
# [10, "A", True].sort()
