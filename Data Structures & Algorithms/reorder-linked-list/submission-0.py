# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #handling empty or just single-node
        if not head or not head.next:
            return 

        #Step1 find the middle using two pointers
        #slow moves one step , fast two steps
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next


        #Step 2 : Split the list into two halves
        second = slow.next 
        slow.next = None

        prev = None

        while second:
            nxt = second.next   # Save node 5
            second.next = prev  # Change 4 → None
            prev = second       # prev points to 4
            second = nxt

        # Step 4: Merge alternately
        # Save both next nodes before changing links
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2





        