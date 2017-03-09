# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        class ListNode(object):
            def __init__(self, x):
                self.val = x
                self.next = None
        if not l1 and not l2:
            return None

        INI = Node = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                # Node.val = l1.val
                Node.next = l1
                l1 = l1.next
            else:
                # Node.val = l2.val
                Node.next = l2
                l2 = l2.next
            Node = Node.next
        if not l1:
            Node.next = l2
        else:
            Node.next = l1
        return INI.next
s = Solution()
print s.mergeTwoLists([2], [1])


