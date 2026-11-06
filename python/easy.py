# Question 1: Student Marks Calculator
# Write a Python program using a function to:
# 1. Store marks in three subjects: 80, 70, 90.
# 2. Calculate the total marks.
# 3. Calculate the average.
# 4. Display the total and average.

def marks():
    m1=80
    m2=70
    m3=90
    marks = m1+m2+m3
    avg=marks/3

    print("total marks" , marks)
    print("avg marks",avg)
marks()
