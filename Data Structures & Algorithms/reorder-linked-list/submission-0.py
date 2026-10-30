# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow=head
        fast=head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # middle is slow

        prev=None
        curr=slow.next
        slow.next=None
        while curr:
            nxt_node=curr.next
            curr.next=prev
            prev=curr
            curr=nxt_node
        
        #prev is the start of the reversed linked list

        curr1=head
        curr2=prev

        while curr2:

            nxt1=curr1.next
            nxt2=curr2.next

            curr1.next=curr2
            curr2.next=nxt1

            curr1=nxt1
            curr2=nxt2
        
      




            



            







