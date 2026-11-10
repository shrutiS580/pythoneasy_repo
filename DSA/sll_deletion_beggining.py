class node ():
    def __init__(self,data):
        self.data = data
        self.next = None

def sll():
    n1 = node(10)
    n2=node(20)
    n3=node(30)

    n1.next =n2
    n2.next =n3

    head = n1 
    head = head.next
    current = head 

    while current is not None:
        print(current.data , end= "-> ")
        current=current.next
    print(None)
sll()        