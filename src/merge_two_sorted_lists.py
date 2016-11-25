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
# time: 2016-11-25

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        lr = ListNode('head')
        pr = lr
        while p1 or p2:
            if p1 and p2:
                if p1.val >= p2.val:
                    pr.next = p2
                    p2 = p2.next
                else:
                    pr.next = p1
                    p1 = p1.next
            elif p1 and not p2:
                pr.next = p1
                p1 = p1.next
            elif p2 and not p1:
                pr.next = p2
                p2 = p2.next
            pr = pr.next
        return lr.next

# l1 = ListNode(1)
# l2 = ListNode(2)
# l3 = ListNode(3)
# l1.next = l2
# l2.next = l3
#
# l4 = ListNode(2)
# l5 = ListNode(5)
# l4.next = l5
#
# lr = Solution().mergeTwoLists(l1, l4)
#
# while lr:
#     print lr.val
#     lr = lr.next
