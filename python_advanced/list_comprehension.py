import os

list_a = [1, 2, 3]

print(list_a)

list_a = list(range(1, 11))

print(list_a)

list_a = []

for x in range(1, 11):
    list_a.append(x * x)

print(list_a)

list_b = [x * x for x in range(1, 11)]

print(list_b)

list_c = [f for f in os.listdir('.')]

print(list_c)

list_c = [f for f in os.listdir('.') if os.path.isfile(f)]

print(list_c)

list_a = [x for x in range(1, 11) if x % 2 == 0]

print(list_a)

list_d = [m + n + i for m in 'ABC' for n in 'XYZ' for i in '123']

# for m in 'ABC':
#     for n in 'XYZ':
#         list_d.append(m + n)

print(list_d)

d = {'a':'X', 'b':'Y', 'c':'Z'}

list_e = [k + '=' + v for k, v in d.items()]

print(list_e)

list_f = ['Hello', 'World']

list_f = [x.lower() for x in list_f]
# lower 大写字母转换成小写

print(list_f)


