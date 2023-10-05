print("command :", "python")
print("sys.argv :", [""], "\n")

print("command :", "python example.py arg1 arg2")
print("sys.argv :", ["example.py", "arg1", "arg2"], "\n")

print("command :", 'echo "import sys; print(sys.argv)" | python -')
print("sys.argv :", ["-"], "\n")

print("command :", "python -c 'import sys; print(sys.argv)' arg1 arg2")
print("sys.argv :", ["-c", "arg1", "arg2"], "\n")

print("python -m module arg1 arg2")
print("sys.argv :", [".../path_to/module.py", "arg1", "arg2"], "\n")
