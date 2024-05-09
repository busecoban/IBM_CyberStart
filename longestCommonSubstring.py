class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLength = 1
        start = 0

        for i in range(n):
            for j in range(i, n):
                flag = 1

                for k in range(0, ((j - i) // 2) + 1):
                    if (s[i + k] != s[j - k]):
                        flag = 0

                if (flag != 0 and (j - i + 1) > maxLength):
                    start = i
                    maxLength = j - i + 1

        return s[start:start + maxLength]
