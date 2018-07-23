class Solution(object):
    def flatten(self, head):
        
        stack=[]
        curr=head
        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next=curr.child
                curr.child=None
                
                curr.next.prev=curr
                
            if not curr.next and stack:
                curr.next=stack.pop()
                curr.next.prev=curr
            
            curr=curr.next
            
        return head
