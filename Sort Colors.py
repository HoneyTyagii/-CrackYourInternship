class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l,r = 0,len(nums)-1
        for i in range(2):
            r = len(nums)-1
            while l <= r:
                if nums[l] == i:
                    l += 1
                elif nums[r] == i:
                    nums[l],nums[r] = nums[r],nums[l]
                    l += 1
                    r -= 1
                else:
                    r -= 1