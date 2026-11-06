# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def sum (num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i] +num [j] == target:
                return [i,j]
num = [2,3,4,5,6]
target= 7            
print (sum(num ,target))