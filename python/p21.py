# # Decorators – *args and **kwargs

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Function started")
#         func(*args, **kwargs)
#         print("Function ended")
#     return wrapper


# @decorator
# def student(name, marks):
#     print(name, marks)


# student("Shruti", 90)
# *args handles multiple positional arguments.
# **kwargs handles multiple keyword arguments
# def decor(func):
#     def wrapper(*args):
#         print("Start")
#         func(*args)
#         print("Finish")
#     return wrapper


# @decor
# def multiply(a, b, c):
#     print(a * b * c)


# multiply(2, 3, 4)
def decor(func):
    def wrapper(n):
        result = func(n)
        return result * 2
    return wrapper


@decor
def square(n):
    return n * n


print(square(5))