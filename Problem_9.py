# coding=utf-8
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False
        elif x == 0:
            return True
        else:
            list = []
            while x //10 != 0:
                list.append(x % 10)
                x = x // 10
            list.append(x)

            i = 0
            j = list.__len__()-1
            while j > i:
                if list[i] == list[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True