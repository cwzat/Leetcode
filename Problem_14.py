class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 前缀初始化为第一个字符，这只能是最长的，只能删减，不能添加
        L = len(strs)
        if L == 0:
            return ""

        res = strs[0]
        length = len(res)
        pos = 0

        while pos <= length-1:
            for i in strs:
                if pos >= len(i) or res[pos] != i[pos]:# 判断的先后顺序
                    return res[:pos]
            pos += 1
        return res[:pos]
