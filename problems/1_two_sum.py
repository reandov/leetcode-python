from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for idx, number in enumerate(nums):
            if number not in hash:
                hash[number] = idx

            if target - number in hash and hash[target - number] != idx:
                return [hash[target - number], idx]

        return []


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(solution.twoSum([3, 2, 4], 6))  # [1, 2]
print(solution.twoSum([3, 3], 6))  # [0, 1]
