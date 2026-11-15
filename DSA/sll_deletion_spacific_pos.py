class node:
    def __init__(self,data):
        self.data = data
        self.next = None
def sll():
    n1 =node(5)
    n2 =node(10)
    n3 =node(15)
    n4 =node(20)

    n1.next =n2
    n2.next=n3
    n3.next=n4

    head =n1
    position = 3
    current = head 

    for i in range(position-2):
        current=current.next
    current.next=current.next.next    
    current = head 

    while current is not None:
        print(current.data , end= " -> ")
        current =current.next
    print(None)
sll()       





        