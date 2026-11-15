class node():
    def __init__(self,data):
        self.data=data
        self.next=None
def ssl():
    n1=node(10)
    n2=node(20)
    n3=node(30)

    n1.next=n2
    n2.next=n3

    head=n1
    position = 2
    current=head

    for i in range(position-2):
        current=current.next
    current.next=current.next.next    
    current=head 

    while current is not None:
        print(current.data,end="--> ")
        current=current.next

    print(None)
ssl()




 
         