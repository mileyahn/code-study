class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            n2 = target - n
            if n2 in dic:
                return [dic[n2], i]
            dic[n] = i