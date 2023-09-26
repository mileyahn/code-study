class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = []
        for stone in stones:
            heappush(s, (-stone, stone))

        while len(s) > 1:
            x = heappop(s)[1]
            y = heappop(s)[1]
            if x != y:
                heappush(s, (y-x, -(y-x)))
            elif len(s) == 0:
                return 0

        return s[0][1]
