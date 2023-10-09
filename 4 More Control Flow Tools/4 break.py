for item in ["a", "b", "c"]:
    for n in range(100):
        if n == 2:
            break
        print(item, n, end=", ")
