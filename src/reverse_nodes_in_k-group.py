# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # head = self.convert_to_list(head)
        res = self.main(head, k)
        print res
        return self.convert_to_link(res)

    def main(self, head, k, res=[]):
        lh = len(head)
        if lh < k:
            res.extend(head)
            return res
        for i in xrange(k // 2):
            head[i], head[k-i-1] = head[k-i-1], head[i]
        res.extend(head[:k])
        if lh > k:
            self.main(head[k:], k, res)
        return res

    def convert_to_list(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    def convert_to_link(self, res):
        lh = head = ListNode(-1)
        for itm in res:
            head.next = ListNode(itm)
            head = head.next
        return lh.next


h = Solution().reverseKGroup([1,2], 2)

while h:
    print h.val
    h = h.next