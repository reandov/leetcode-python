from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


def print_linked_list(head: ListNode):
    visited = set()
    while head:
        if head in visited:
            print(f"{head.val} -> ... (cycle detected)")
            return
        print(head.val, end=" -> ")
        visited.add(head)
        head = head.next
    print("None")


# Creating a linked list with a cycle manually
head_with_cycle = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head_with_cycle.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2  # Creates a cycle

# Creating a linked list without a cycle
head_without_cycle = ListNode(
    1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))
)

solution = Solution()

print_linked_list(head_with_cycle)
print("Has Cycle:", solution.hasCycle(head_with_cycle))

print_linked_list(head_without_cycle)
print("Has Cycle:", solution.hasCycle(head_without_cycle))
