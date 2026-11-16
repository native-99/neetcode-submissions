
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # Step 1: Store all nodes in an array
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        # Step 2: Use two pointers
        left = 0
        right = len(nodes) - 1
        order = []

        # Step 3: Take front and back alternately
        while left <= right:
            order.append(nodes[left])
            left += 1

            if left <= right:
                order.append(nodes[right])
                right -= 1

        # Step 4: Reconnect the nodes
        for i in range(len(order) - 1):
            order[i].next = order[i + 1]

        # The last node must point to None
        order[-1].next = None
