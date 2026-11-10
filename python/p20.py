# def decorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("After function")
#     return wrapper


# @decorator
# def greet():
#     print("Hello Shruti!")


# greet()
def decorator(func):
    def wrapper(a, b):
        print("Addition started")
        func(a, b)
        print("Addition completed")
    return wrapper


@decorator
def add(a, b):
    print(a + b)


add(10, 20)