class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = Counter(list(s))

        one = count['1']
        zero = count['0']

        return '1' * (one-1) + '0' * zero + '1'