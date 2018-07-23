class Solution(object):
    def addTwoNumbers(self, l1, l2):

        num1=[]
        num2=[]
        p,q=l1,l2
        
        while p or q:
            if p:
                num1.append(p.val)
                p=p.next
            if q:
                num2.append(q.val)
                q=q.next
        head=ListNode(-1)
        carry=val=0


 
