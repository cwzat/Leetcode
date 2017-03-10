# coding=utf-8
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums.sort()
        # list.sort()函数没有返回值
        length = len(nums)
        flag = False
        for i in nums:
            if i == val:
                flag = True
        pos = 0
        if not flag or length == 0:
            return length
        else:
            while pos <= len(nums)-1:
                if nums[pos] == val:
                    del nums[pos]
                else:
                    pos += 1

        return len(nums)
s = Solution()
print s.removeElement([1, 2, 2, 2, 3], 2)