class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, j in enumerate(nums):
            compliment = target - j
            if compliment in map:
                return [map[compliment], i]
            map[j] = i