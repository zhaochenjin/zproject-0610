class Human(object):
    __slots__ = ('name', 'age')
    pass

tom = Human()
tom.name = 'Tom'

print(tom.name)

tom.age = 18
print(tom.age)

tom.gender = 'Male'
print(tom.gender)


