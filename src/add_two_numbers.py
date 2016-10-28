# coding: utf-8

# author: RaPoSpectre
# time: 2016-09-20

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def system_change(self, l3):
        pp = l3
        while True:
            if l3.val >= 10:
                l3.val = l3.val - 10
                tm, l3 = l3, l3.next
                if not l3:
                    tm.next = ListNode(1)
                else:
                    l3.val += 1
            else:
                l3 = l3.next
            if not l3:
                return pp

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        p3 = p3h = None
        while True:
            if p1 and p2:
                if p3:
                    p3.next = ListNode(p1.val + p2.val)
                    p3 = p3.next
                else:
                    p3h = p3 = ListNode(p1.val + p2.val)
            p1 = p1.next
            p2 = p2.next
            if p1 and not p2:
                p2 = ListNode(0)
            if p2 and not p1:
                p1 = ListNode(0)
            if not (p1 and p2):
                return self.system_change(p3h)
