class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums) / 2
        count = {}

        for i in nums:
            print(i)
            if count.get(i) is None:
                count[i] = 0
            count[i] += 1
            if count[i] > target:
                return i    
            
        return -1