import sys

print(sys.argv);

for file in sys.argv[1:]:
    with open(file, "w") as f:
        print(f.readlines())