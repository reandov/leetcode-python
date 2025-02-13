class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        right = 0
        counter = {}
        counter[s[0]] = 1
        max = 0

        while right < len(s) - 1:
            right += 1

            if s[right] in counter:
                counter[s[right]] += 1
            else:
                counter[s[right]] = 1

            while counter[s[right]] == 3:
                counter[s[left]] -= 1
                left += 1

            if max < sum(counter.values()):
                max = sum(counter.values())

        return max
    
# Testing
solution = Solution()
print(solution.maximumLengthSubstring("bcbbbcba"))
print(solution.maximumLengthSubstring("aaaa"))