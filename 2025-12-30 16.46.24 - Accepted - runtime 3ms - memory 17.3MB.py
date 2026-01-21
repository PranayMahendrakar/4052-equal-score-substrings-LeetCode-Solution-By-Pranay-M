class Solution:
    def scoreBalance(self, s: str) -> bool:
        total = sum(ord(c) - ord('a') + 1 for c in s)
        if total % 2 != 0:
            return False
        target = total // 2
        prefix_sum = 0
        for i in range(len(s) - 1):  # -1 because both parts must be non-empty
            prefix_sum += ord(s[i]) - ord('a') + 1
            if prefix_sum == target:
                return True
        return False