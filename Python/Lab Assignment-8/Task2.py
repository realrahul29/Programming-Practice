# b) Copy without comments
src = input("Source file: ")
dest = input("Destination file: ")

with open(src, "r") as f:
    lines = f.readlines()

with open(dest, "w") as f:
    for line in lines:
        if not line.strip().startswith("#"):
            f.write(line)