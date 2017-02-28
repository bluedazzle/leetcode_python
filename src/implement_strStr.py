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
# time: 2017-02-28

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return self.sunday(haystack, needle)

    def sunday(self, s, model):
        match = False
        ms = 0
        me = len(model)

        if s == model:
            # print '匹配成功,位置: s[{0}]->s[{1}]'.format(0, len(model))
            return ms

        while 1:
            p = s[ms: me]
            if model == p:
                match = True
                # print '匹配成功,位置: s[{0}]->s[{1}]'.format(ms, me)
                break
            if me >= len(s):
                break
            sign = s[me]
            if sign in model:
                posi = model.rfind(sign)
                offset = len(model) - posi
                ms += offset
                me += offset
            else:
                ms += len(model)
                me += len(model)
        if match:
            return ms
        return -1


# print Solution().strStr('123', '42')
