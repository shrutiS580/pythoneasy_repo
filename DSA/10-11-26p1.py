# class node():
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# def sll():
#     n1 = node(10)
#     n2=node(20)
#     n3=node(30)

#     n1.next=n2
#     n2.next=n3

#     head = n1 
    
#     new_node = node(40)
#     current = head 
#     while current.next is not None:
#         current = current.next
#     current.next =new_node    
#     current = head
   
#     while current is not None:
#         print(current.data , end= " --> ")
#         current=current.next
#     print(None)   
# sll()     
class node():
    def __init__(self,data):
        self.data = data
        self.next = None
def sll():
    n1=node(10)
    n2=node(20)
    n3=node(30)

    n1.next = n2
    n2.next = n3

    head = n1 
    new_node = node(40)
    current = head 
    while current.next is not None:
        current = current.next
    current.next =new_node
    current = head     

    while current is not None:
        print(current.data,end=" -> ")
        current=current.next
    print(None)

sll()                