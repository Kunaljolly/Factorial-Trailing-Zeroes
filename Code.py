class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        c = 0
        r = n
        while r >= 5:
            r = n // 5
            c += r
            n = r
        return c
