import subprocess

print("which python:")
print(subprocess.run(["which", "python"], capture_output=True, text=True).stdout)

print("python --version:")
print(subprocess.run(["python", "--version"], capture_output=True, text=True).stdout)

print("^p | interactive editing")
print("uses - GNU readline", "\n")

print("-c | command")
print("python -c 'print(2 + 3)'", "\n")

print("-m | module")
print("python -m pip list", "\n")

print("-i | interactive")
print("python -i script.py", "\n")
