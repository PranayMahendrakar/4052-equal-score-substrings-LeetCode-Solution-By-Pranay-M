class Solution:
    def scoreBalance(self, s: str) -> bool:
        total = sum(ord(c) - ord('a') + 1 for c in s)
        prefix = 0
        for i in range(len(s) - 1):  # Can't include last char in prefix
            prefix += ord(s[i]) - ord('a') + 1
            if prefix == total - prefix:
                return True
        return False