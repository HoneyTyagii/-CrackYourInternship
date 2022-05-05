class Solution(object):
   def findDuplicate(self, nums):
      hare = nums[0]
      tortoise = nums[0]
      while True:
         hare = nums[nums[hare]]
         tortoise = nums[tortoise]
         if hare == tortoise:
            break
      ptr = nums[0]
      while ptr!=tortoise:
         ptr = nums[ptr]
         tortoise = nums[tortoise]
      return ptr
ob1 = Solution()
print(ob1.findDuplicate([3,1,3,4,2]))