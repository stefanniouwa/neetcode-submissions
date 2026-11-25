class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            hashmap[num] = i

        for i, num in enumerate(nums):
            desired = target - num
            if desired in hashmap and hashmap[desired] != i:
                return [i, hashmap[desired]]