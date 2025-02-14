from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for position, number in enumerate(nums):
            if position > k:
                window.remove(nums[position - k - 1])

            if number in window:
                return True

            window.add(number)

        return False


solution = Solution()
print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))  # True
print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))  # True
print(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # False
