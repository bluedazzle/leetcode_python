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
# time: 2016-11-15

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        lp = head
        link_list = [lp]
        while lp.next:
            link_list.append(lp.next)
            lp = lp.next
        n = len(link_list) - n
        if len(link_list) == 1:
            return None
        if n == len(link_list) - 1:
            link_list[n-1].next = None
        elif n == 0:
            link_list.pop(0)
        else:
            link_list[n-1].next = link_list[n+1]
        return link_list[0]


#
#
# l1 = ListNode(1)
# l2 = ListNode(2)
# l1.next = l2
# l3 = ListNode(3)
# l2.next = l3
# l4 = ListNode(4)
# l3.next = l4
#
# p = Solution().removeNthFromEnd(l1, 2)
# print p.val
