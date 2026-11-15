# Question 1: Create a singly linked list containing:
# 5 → 10 → 15 → 20 → 25 → None
# delete node at positio 2 
class node():
    def __init__(self,data):
        self.data = data 
        self.next = None
def list():
    n1 =node(5)
    n2 =node(10)
    n3 =node(15)
    n4 =node(20)
    n5 =node(25)

    n1.next=n2
    n2.next=n3
    n3.next=n4
    n4.next=n5

    head = n1 
    position = 2
    current =head

    for i in range(position -2):
        current =current.next
    current.next =current.next.next

    while current is not None:
        print(current.data , end= " -> ")
        current=current.next

    print(None)

list()        

    