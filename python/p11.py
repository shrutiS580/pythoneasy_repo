def student(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student(name="Shruti", age=22, marks=90)