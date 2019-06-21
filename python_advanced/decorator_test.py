# def a_decorator(func):
#
#     def wrapper():
#         print(func.__name__, 'before...')
#         func()
#         print(func.__name__, 'after...')
#
#     return wrapper
#
#
# def f():
#     print('function f...')
#
# # f()
#
# a_decorator(f)
# print("-----------------------")
# print(a_decorator(f))
# print("-----------------------")
# a_decorator(f)()
# print("-----------------------")


def a_decorator(func):

    def wrapper(*args, **kwargs):  # arguments
        print(func.__name__, 'before...')
        func(*args, **kwargs)
        print(func.__name__, 'after...')

    return wrapper


@a_decorator
def f():
    print('function f...')


@a_decorator
def foo(name):
    print('hi', name)

# f = a_decorator(f)

f()

foo('Tom')