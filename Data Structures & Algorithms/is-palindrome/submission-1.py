class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [char.lower() for char in s if char.isalnum()]
        return filtered[::-1] == filtered