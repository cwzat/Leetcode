# coding=utf-8
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        if length == 0 or length % 2 != 0:
            return False
        # for i in s:
        #    if i != ')' or i != '(' or '[' or ']' or '{' or '}':
        #       return False

        list = []
        dic = {'(': ')', '[': ']', '{': '}'}
        for i in s:
            if i == '(' or i == '[' or i == '{':# 或的表达式要写全
                list.append(i)
            elif i == ')' or i == ']' or i == '}':
                if len(list) != 0:
                    if dic[list[-1]] == i:
                        list.pop()
                    else:
                        return False
            else:
                return False
        if list.__len__() != 0:
            return False
        else:
            return True

s = Solution()
print s.isValid("){")


