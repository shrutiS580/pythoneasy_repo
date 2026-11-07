# Write a Python program using a lambda function to find the cube of a number
# def cube():
#     cube = lambda n:n*n*n
#     print(cube(7))
# cube() 
# ---------------------------------------------------------------------
# Write a Python program using a lambda function to find 
# the square of two numbers and print their sum   
# def fun():
#     fun=lambda a,b:a*a + b*b
#     print(fun(2,6))
# fun()    
# ----------------------------------------------------------------------------
# Write a Python program using lambda to check whether a number is positive, negative or zero

# def chk():
#     chk = lambda n: "positive" if n>=0 else "negative"
#     print(chk(-8))
# chk()    
# --------------------------------------------
# Write a Python program using lambda to find the largest of three numbers.
# def largestofthree():
#     largestofthree = lambda a,b,c : a if a>b and a>c else (b if b>a and b>c else c)
#     print(largestofthree(34,45,60))
# largestofthree()    
# -------------------------------------------------------------------------------------
# Write a Python program using lambda to check whether a student has passed or failed.
# - Marks = 65
# - Passing marks = 40
# - If marks are 40 or above → Pass
# - Otherwise → Fail
def student():
    student = lambda marks: "pass" if marks >=40 else "fail"
    print(student(65))
student()    