x = 0
while x < 3:
    print(x)
    x += 1
else:
    print(x, "done")

print("----------")

for i in range(3):
    print(i)
else:
    print(i, "done")

print("----------")

for i in range(1, 10, 2):
    if i % 2 == 0:
        print("even number found, break at", i)
        break
    else:
        print("odd number", i)
else:
    print("all odd numbers")
