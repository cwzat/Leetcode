# coding=utf-8
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integerTmp = dictionary[s[-1]]
        tmp = s[-1]
        for i in range(len(s)-2, -1, -1):
            # range()'s end is not in the cycle
            if dictionary[s[i]] >= dictionary[tmp[-1]]:
                integerTmp += dictionary[s[i]]
            else:
                integerTmp -= dictionary[s[i]]
            tmp += s[i]
        return integerTmp