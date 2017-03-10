# coding=utf-8
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0 or length == 1:
            return length
        # 现在列表的元素最少是两个
        i = 0
        while i < len(nums)-1:
            # while nums[i+1]代表的是访问不到就越界了，而不是访问不到就退出循环
            # 所以判断是否在列表内就用小于长度
            if nums[i] == nums[i+1]:
                # 这个语句已经把最后一个判断了，只要访问到最后一个元素就可以退出了
                # 使用del 删除对应下标的元素 使用pop删除最后一个元素
                del nums[i]
                # i = 0
                # 注意这个语句的错误
            else:
                i += 1
        res = len(nums)
        return res


s = Solution()
print s.removeDuplicates([1, 2, 2, 2, 3, 4, 4, 4])