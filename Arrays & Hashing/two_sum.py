class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for start in range(len(nums)):
            req = target - nums[start]
            if req in nums[start+1:]:
                return [start, nums[start+1:].index(req)+start+1]