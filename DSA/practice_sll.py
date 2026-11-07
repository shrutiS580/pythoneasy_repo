# class node():
#     def __init__(self , data):
#         self.data = data
#         self.next = None

# def display():
#     n1 =node(5)
#     n2 =node(10)
#     n3 =node(15)
#     n4 =node(20)
#     n5 =node(25)

#     n1.next =n2
#     n2.next =n3
#     n3.next =n4
#     n4.next =n5

#     head = n1 
#     new_node=node(1)
#     new_node.next=head
#     head = new_node

#     current = head 

#     while current is not None:
#         print(current.data , end = " -> ")
#         current = current.next
#     print(None)
# display()    

class node():
    def __init__(self,data):
        self.data = data
        self.next = None

def display():
    n1=node(1)
    n2=node(2)
    n3=node(3)
    n4=node(4)

    n1.next =n2
    n2.next= n3
    n3.next =n4

    head = n1
    new_node = node(0)
    new_node.next=head
    head =new_node


    current = head 

    while current is not None:
        print(current.data , end = "-> ")
        current=current.next
    print(None)    

display()       
        

























    