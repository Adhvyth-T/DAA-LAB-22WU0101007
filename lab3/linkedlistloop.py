class cirlinkedlist:
    def __init__(self,head):
        self.curr=head
    def traverse(self):
        curr1=self.curr
        curr2=self.curr.next
        b=True
        c=0
        while b:
            if curr1.data==curr2.data:
                b=False
                print("loop found")
            else:
                curr1=curr1.next
                curr2=((curr2.next).next).next
                c+=1
            if c==60:
                print("no loop")
                break



class Node:
    def __init__(self,val):
        self.data=val
        self.next=None



head=Node(10)
n1=Node(20)
head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n3.next=n1
k=cirlinkedlist(head)
k.traverse()

        
