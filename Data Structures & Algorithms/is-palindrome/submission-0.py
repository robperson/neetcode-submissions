class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized = "".join([ch.lower() for ch in s if ch.isalnum()])
        return sanitized == sanitized[::-1]
        