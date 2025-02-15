# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None

        while head:
            next_node = head.next
            head.next = new_list
            new_list = head
            head = next_node

        return new_list


def print_linked_list(head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    print(values)


solution = Solution()
reversed_linked_list = solution.reverseList(
    head=ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
)

print_linked_list(reversed_linked_list)  # Expected: [5, 4, 3, 2, 1]
