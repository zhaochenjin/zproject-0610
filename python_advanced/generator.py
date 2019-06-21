list_a = list(range(1, 11))

print(list_a)

list_a = [x**2 for x in range(1, 11)]

print(list_a)

for x in list_a:
    print(x)


g_a = (x**2 for x in range(1, 5))

print(type(g_a))

# print(g_a)

# print(next(g_a))
# print(next(g_a))
# print(next(g_a))
# print(next(g_a))

# print(next(g_a))


for n in list_a:
    print('n:', n)

for n in g_a:
    print('n:', n)

print('---------------')

for n in list_a:
    print('n:', n)

for n in g_a:
    print('n:', n)