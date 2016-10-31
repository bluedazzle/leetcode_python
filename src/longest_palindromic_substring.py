# coding: utf-8

# author: RaPoSpectre
# time: 2016-10-31


# 将每个字符串当作回文串的中心进行验证

class Solution(object):
    def find_from_center(self, s, ms, cs):
        jts = ''
        ots = ''
        j = True
        o = True
        for i in xrange(0, ms + 1):
            if s[cs - i] == s[cs + i] and j:
                jts = s[cs - i: cs + i + 1]
            else:
                j = False
            if ms + cs + 1 == len(s) and i == ms:
                break
            if s[cs - i] == s[cs + i + 1] and o:
                ots = s[cs - i: cs + i + 2]
            else:
                o = False
        if len(ots) > len(jts):
            return ots
        return jts

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rs = ''
        for i in xrange(0, len(s)):
            ts = i
            te = len(s) - i - 1
            if ts < te:
                tmp = self.find_from_center(s, ts, i)
            else:
                tmp = self.find_from_center(s, te, i)
            if len(tmp) > len(rs):
                rs = tmp
        return rs
