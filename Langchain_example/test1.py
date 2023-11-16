"""

链表排序
"""
class ListNode(object):
    def __init__(self,val,next=None):
        self.val=val
        self.next=next


def line_sort(head):
    pre=ListNode(-9999999)
    pre.next=head

    sum=0
    t=pre
    while t!=None:
        t=t.next
        sum+=1

    for i in range(sum):
        t=pre
        now=pre.next
        while now.next!=None:
            n=now.next
            if n.val<now.val:
                nn=n.next
                n.next=now
                now.next=nn
                t.next=n
            t=now
            now=now.next

    return pre.next

def show_list(head):
    while head !=None:
        print(head.val)
        head=head.next

def main():
    head=ListNode(23,ListNode(30,ListNode(-2,(ListNode(200)))))
    show_list(head)
    print('-----------------------------------------')
    head=line_sort(head)
    show_list(head)

if __name__=="__main__":
    main()






