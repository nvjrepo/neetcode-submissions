class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [char.lower() for char in s if char.isalnum()]
        a = True
        i = 0
        j = len(filtered) - 1
        while i < j:
            if filtered[j] != filtered[i]:
                a = False
                break
            i = i + 1
            j = j - 1
        return a