# Definition for singly-linked list.
import copy


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        pl = cur = head
        h_list = []
        tmpl = None
        while 1:
            for i in xrange(k):
                if not pl:
                    break
                tmpl = pl
                pl = pl.next
            if not tmpl and not pl:
                h_list.append(cur)
                break
            if not cur:
                break
            pre = cur
            cur = cur.next
            pre.next = None
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
                if cur == pl:
                    h_list.append(pre)
                    break
        sp = Node(-1)
        for itm in h_list:
            sp.next = itm
            while itm:
                if not itm.next:
                    sp = itm
                itm = itm.next

        return h_list[0]


l = Solution().reverseKGroup(link, 4)
while l:
    print l.data
    l = l.next
