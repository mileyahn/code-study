class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output, heap = [], []

        for point in points:
            x, y = point[0], point[1]
            heappush(heap, (x**2 + y**2, point))

        for i in range(k):
            output.append(heappop(heap)[1])
            
        return output
        