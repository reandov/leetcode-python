from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ahead = head
        while ahead and ahead.next:
            ahead = ahead.next.next
            head = head.next

        return head


def print_linked_list(head: ListNode):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


solution = Solution()
print_linked_list(
    solution.middleNode(
        head=ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    )
)
print_linked_list(
    solution.middleNode(
        head=ListNode(
            1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))
        )
    )
)
