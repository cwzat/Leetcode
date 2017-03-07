# coding=utf-8
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        maximum = 2**31 - 1
        minimum = -(2**31 - 1)

        str_x = str(x)
        rev_x = str_x[::-1]

        if x >= 0:
            tmp = int(rev_x)
        else:
            list = ""
            list = list + rev_x[-1]
            list = list + rev_x[0:len(rev_x)-1]
            tmp = int(list)

        if tmp > maximum or tmp < minimum:
            return 0
        else:
            return tmp