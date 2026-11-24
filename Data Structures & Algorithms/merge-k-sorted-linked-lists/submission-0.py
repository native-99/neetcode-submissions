class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge_two(a, b):
            dummy = ListNode(0)
            tail = dummy

            while a and b:
                if a.val <= b.val:
                    tail.next = a
                    a = a.next
                else:
                    tail.next = b
                    b = b.next

                tail = tail.next

            if a:
                tail.next = a
            else:
                tail.next = b

            return dummy.next

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                a = lists[i]
                b = lists[i + 1] if i + 1 < len(lists) else None

                merged.append(merge_two(a, b))

            lists = merged

        return lists[0] if lists else None