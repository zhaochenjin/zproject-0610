import os

# name = input('your name:')

# print(name)

with open('day01.py') as f:
    # print(type(f.readlines()))
    for line in f.readlines():
        # print(line.strip())
        pass

print([x for x in os.listdir('.') if os.path.isfile(x)])