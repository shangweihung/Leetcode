class Solution(object):
    def numComponents(self, head, G):

        num_of_groups=0
        g_set=set(G)
        while head:
            if head.val in g_set and (not head.next or head.next.val not in g_set) :
                                      # the lase part   # meet the element not in G
                num_of_groups+=1
            head=head.next          

        return num_of_groups
