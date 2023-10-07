class MedianFinder:

    def __init__(self):
        self.head = [] # 큰 순서대로
        self.back = []
        self.cnt = [0, 0]

    def addNum(self, num: int) -> None:
        if self.back and num > self.back[0]:
            heappush(self.back, num)
            self.cnt[1] += 1
        else:
            heappush(self.head, -1*num)
            self.cnt[0] += 1
        
        if self.cnt[0] > self.cnt[1]+1:
            heappush(self.back, -1*heappop(self.head))     
            self.cnt[1] += 1
            self.cnt[0] -= 1
        if self.cnt[0]+1 < self.cnt[1]:
            heappush(self.head, -1*heappop(self.back))
            self.cnt[0] += 1
            self.cnt[1] -= 1

    def findMedian(self) -> float:
        if sum(self.cnt) % 2 == 0:
            return (-1*self.head[0] + self.back[0])/2
        elif self.cnt[0] < self.cnt[1]:
            return self.back[0]
        else:
            return -1*self.head[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()