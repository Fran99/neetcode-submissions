class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # create a helper hm to store count
        times = {}

        # Iterate over nums
        for num in nums:
            if num not in times:
                times[num] = num
            else: 
                return True

        return False            