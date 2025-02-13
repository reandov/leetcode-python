class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        left, right = 0, 0

        while right < len(s):
            if s[right] != " ":
                right += 1
            else:
                result += s[left : right + 1][::-1]
                right += 1
                left = right

        result += " "
        result += s[left : right + 2][::-1]

        return result[1:]

# Testing
solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))
print(solution.reverseWords("Mr Ding"))