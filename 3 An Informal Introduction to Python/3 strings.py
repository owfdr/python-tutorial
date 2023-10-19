from icecream import ic
from termcolor import colored

print("''", "single quotes")
print('""', "double quotes")
print("(both yield same results)")
print("\\", "escape quotes")
print(r"r''", "raw string")
print("'''", '"""', "multi-line string")
print("\\", "prevent new line")
print("+", "concatenate")
print("*", "repeat")
print('"a" "pple"', ("a" "pple"))
print("(useful for long strings)")

print("---------- indexed")

ic("python"[0])
ic("python"[5])
print('"python"[6]', colored("IndexError: string index out of range", "magenta"))

ic("python"[-1])
ic("python"[-6])
print('"python"[-7]', colored("IndexError: string index out of range", "magenta"))

print("---------- slicing")

ic("python"[0:2], "-> length 2")
ic("python"[2:6], "-> length 4")
ic("python"[0:100], "(handled gracefully)")

ic("python"[:2] + "python"[2:])
ic("python"[:-4] + "python"[-4:])

print(
    'python[0] = "P"',
    colored("TypeError: 'str' object does not support item assignment", "magenta"),
    "(immutable)",
)

print("---------- built-in function")

ic(len("python"))
