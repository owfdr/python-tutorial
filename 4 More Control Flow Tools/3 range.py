from icecream import ic

print("- for index in range(3):")
for index in range(3):
    print(range(3), index)

print("- for index in range(1, 4):")
for index in range(1, 4):
    print(range(1, 4), index)

print("- for index in range(2, 11, 2):")
for index in range(2, 11, 2):
    print(range(2, 11, 2), index)

phonetics = ["alpha", "bravo", "charlie"]

print("- for index in range(len(phonetics)):")
for index in range(len(phonetics)):
    print(phonetics, index, phonetics[index])

print("- for index, item in enumerate(phonetics):")
for index, item in enumerate(phonetics):
    print(enumerate(phonetics), index, item)

print("- range() returns iterable object, not list.")

ic(sum(range(5)))
ic(sum([0, 1, 2, 3, 4]))
ic(sum(list(range(5))))
