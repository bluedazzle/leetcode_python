# coding: utf-8
#                                                    ##       ##
#                                                  #####   #  ####
#                                               ######### ## #######
#                                              ###  ############ ##
#                               ####          #     ####### #########
#  ###########               #########       #      ###########  ##
# #############             ###    ####        ##  #### ########                                     ##
# ##   ##    ##            ##        ###     #########  #########        ###         ##       #     ###      ##      #
#      ##   ##                    ## ###    ########   ##########       #### ##     ###     ####   ###    #####    ####
#     ## ####                     ##  ##   #########   ##########      ########    #####   ####    ####   #####   #####
#    ######          ####        ##   ##  ### ## ###  ############    ## ### ##   ## ##   ###      ###    #####  ### ##
#    ####           #####        ##  ###  ###  ###### ############       ##  ##  #####    ### ##  ###     ###    #####
#   ## ##         ### ###       ###  ###   ######### ##############     ### ##   ####     ## ###  #####  ####    ####
#   ## ###        ##  ##        ##  ###     #####    ##############    #######    #####   #####   #####  ###     ######
#  ##   ###  ##  #######        ######              ###############    ####         ##     ##       #              ###
#  ##   ######   #######       #####               #################   ###
# ##      ###     ##  ##       ###                  #################  ##
# ##                           ##                 ###################  ##
# ##                          ###                  ######################
#                             ##                    #               ## #
#                             ##
# author: RaPoSpectre
# time: 2016-11-29

from collections import deque


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) <= 1:
            return lists[0] if len(lists) == 1 else None

        def merge(left, right):
            ph = merged = ListNode("head")
            while left or right:
                tmp = ListNode(-1)
                if left and right:
                    if left.val <= right.val:
                        tmp.val = left.val
                        left = left.next
                    else:
                        tmp.val = right.val
                        right = right.next
                elif not right:
                    tmp.val = left.val
                    left = left.next
                elif not left:
                    tmp.val = right.val
                    right = right.next
                merged.next = tmp
                merged = merged.next
            return ph.next

        middle = int(len(lists) // 2)
        left = self.mergeKLists(lists[:middle])
        right = self.mergeKLists(lists[middle:])
        return merge(left, right)

    def generate_node_list(self, node_list):
        res = []
        for itm in node_list:
            ph = head = ListNode(-1)
            for sitm in itm:
                head.next = ListNode(sitm)
                head = head.next
            res.append(ph.next)
        return res

    def main(self, lists):
        res = self.generate_node_list(lists)
        return self.mergeKLists(res)


ph = Solution().main([[1, 2, 3], [4, 5, 6], [1, 2, 6]])
while ph:
    print ph.val
    ph = ph.next
