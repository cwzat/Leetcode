# coding=utf-8
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

       """

        dictionary = {}
        index = 0
        for i in nums:
            j = target - i
            if dictionary.has_key(j):
                '''if we find j,we print the index'''
                List = []
                List.append(dictionary[j])
                dictionary[i] = index
                List.append(dictionary[i])
                return List
            else:
                dictionary[i] = index
            """

            if we don't find the matched elements, we add the current
            into the dictionary

            """

            index += 1