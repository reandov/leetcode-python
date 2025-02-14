class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashset: dict[str, tuple] = {}

        for idx, char in enumerate(s):
            if char not in hashset:
                hashset[char] = [idx, 1]
            else:
                hashset[char][1] += 1

        for char, (index, count) in hashset.items():
            if count == 1:
                return index

        return -1


solution = Solution()
print(solution.firstUniqChar("leetcode"))  # 0
print(solution.firstUniqChar("loveleetcode"))  # 2
print(solution.firstUniqChar("aabb"))  # -1
