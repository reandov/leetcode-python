from typing import List


class Solution:
    def search(
        self, nums: List[int], target: int, left: int = 0, right: int = None
    ) -> int:
        if right is None:
            right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1

    def exponential_search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0

        size = len(nums)
        right = 1

        while right < size and nums[right] < target:
            right *= 2

        if nums[min(right, size - 1)] == target:
            return nums[right]

        return self.search(nums, target, right // 2, min(right, size - 1) - 1)


# Testing
solution = Solution()
# print(solution.search([-1, 0, 3, 5, 9, 12], 9))
# print(solution.search([-1, 0, 3, 5, 9, 12], 2))
print(
    solution.exponential_search(
        [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
        ],
        37,
    )
)
