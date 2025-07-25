class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        for digit in str(num):
            d = int(digit)
            if d != 0 and num % d == 0:
                count += 1
        return count
