class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(map(S.count, J))
        