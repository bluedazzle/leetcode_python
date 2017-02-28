# leetcode python solution

## Algorithms 
(:100: 代表答主提交答案时在前 100 %)

#### 1. [Two Sum][1]: [Solution][2] 
#### 2. [Add Two Numbers][3]: [Solution][4] :100:
#### 3. [Longest Substring Without Repeating Characters][5]: [Solution][6]
#### 4. [Median of Two Sorted Arrays][7]: [Solution][8] :100:
#### 5. [Longest Palindromic Substring][9]: [Solution][10]
(这道题对 Python 有毒, 只要时间复杂度大于等于 O(n2) 绝对 TLE, 其它语言 O(n3) 也能过...)  

**tips: Python 用 Manacher’s Algorithm 比较稳, 其它算法基本 TLE. 本例里用将每个字符当作回文串中心对匹配方式,还是可能 TLE.**
#### 6. [ZigZag Conversion][11]:[Solution][12]
**tips: 以每 (2 * numRows - 2) 个字符串为一组进行操作,最后一组不足 (2 * numRows - 2) 个字符用特殊字符补齐,最后返回前再将特殊字符去掉**
#### 7. [Reverse Integer][13]: [Solution][14]
#### 8. [String to Integer (atoi)][15]: [Solution][16]
#### 9. [Palindrome Number][17]: [Solution][18]
#### 10. [Regular Expression Matching][19]: [Solution][20]
**tips: 用[动态规划][21]的思路可以解, 递归 Python 会 TLE. 用 re 库可以一句话解决: (return re.match(r'^{0}$'.format(p), s)) 不过不推荐.**
#### 11. [Container With Most Water][22]: [Solution][23] :100:
**tips: bf 做复杂度 O(n2) Python 会 TLE. 用两个游标分别从数组首位出发谁小谁移动, 纪录其中最大值, 复杂度 O(n)**
#### 12. [Integer to Roman][24]: [Solution][25]
#### 13. [Roman to Integer][26]: [Solution][27] :100:
#### 14. [Longest Common Prefix][28]: [Solution][29]
**动态规划思路: 复杂度 O(n2), 状态是: n 个字符串 n <= len(strs) 的最长公共前缀, 转移方程: D(n) = min{D(n-1), L(j)}, 0 <= j <= min{D(n-1), len(str(n))} (大概是这样)**
#### 15. [3Sum][30]: [Solution][31] 
**tips: [K Sum Problem][32]**
#### 16. [3Sum Closest][33]: [Solution][34]
**tips: 可以看作是有个固定数字的 4 Sum 问题,稍微改下 3 Sum 代码即可, 时间复杂度不增加 O(nlogn)**
#### 17. [Letter Combinations of a Phone Number][35]: [Solution][36]
**tips: 简单替换后直接算 kronecker 积, 复杂度 O(n)**
#### 18. [4Sum][37]: [Solution][38]
#### 19. [Remove Nth Node From End of List][39]: [Solution][40]
#### 20. [Valid Parentheses][41]: [Solution][42]
#### 21. [Merge Two Sorted Lists][43]: [Solution][44]
#### 22. [Generate Parentheses][45]: [Solution][46]
**tips: backtracking**
#### 23. [Merge k Sorted Lists][47]: [Solution][48]
**tips: [分治法][49] [归并排序][50]**
#### 24. [Swap Nodes in Pairs][51]: [Solution][52]
#### 25. [Reverse Nodes in k-Group][53]: [Solution][54]
#### 26. [Remove Duplicates from Sorted Array][55]: [Solution][56]
**tips1: 虽然只是让返回去除重复后的数组长度,但是oj还是会判断代码是否真的去掉的是重复的元素,否则即使你返回的长度正确oj依然会 WA**  
**tips2: 不能用`len(set(nums))` 一句完成,因为 set 申请了新的空间,而题目要求不能使用新的空间** 
#### 27. [Remove Element][57]: [Solution][58]
#### 28. [Implement strStr()][59]: [Solution][60]
#### 29. [Divide Two Integers][61]: [Solution][62]

[1]: https://leetcode.com/problems/two-sum/
[2]: https://github.com/bluedazzle/leetcode_python/blob/master/src/two_sum.py
[3]: https://leetcode.com/problems/add-two-numbers
[4]: https://github.com/bluedazzle/leetcode_python/blob/master/src/add_two_numbers.py
[5]: https://leetcode.com/problems/longest-substring-without-repeating-characters/
[6]: https://github.com/bluedazzle/leetcode_python/blob/master/src/lswrc.py
[7]: https://leetcode.com/problems/median-of-two-sorted-arrays
[8]: https://github.com/bluedazzle/leetcode_python/blob/master/src/motsa.py
[9]: https://leetcode.com/problems/longest-palindromic-substring/
[10]: https://github.com/bluedazzle/leetcode_python/blob/master/src/longest_palindromic_substring.py
[11]: https://leetcode.com/problems/zigzag-conversion/
[12]: https://github.com/bluedazzle/leetcode_python/blob/master/src/zigzag_conversion.py
[13]: https://leetcode.com/problems/reverse-integer/
[14]: https://github.com/bluedazzle/leetcode_python/blob/master/src/reverse_integer.py
[15]: https://leetcode.com/problems/string-to-integer-atoi/
[16]: https://github.com/bluedazzle/leetcode_python/blob/master/src/string_to_integer.py
[17]: https://leetcode.com/problems/palindrome-number/
[18]: https://github.com/bluedazzle/leetcode_python/blob/master/src/palindrome_number.py
[19]: https://leetcode.com/problems/regular-expression-matching/
[20]: https://github.com/bluedazzle/leetcode_python/blob/master/src/regular_expression_matching.py
[21]: http://www.360doc.com/content/13/0601/00/8076359_289597587.shtml
[22]: https://leetcode.com/problems/container-with-most-water/
[23]: https://github.com/bluedazzle/leetcode_python/blob/master/src/container_with_most_water.py
[24]: https://leetcode.com/problems/integer-to-roman/
[25]: https://github.com/bluedazzle/leetcode_python/blob/master/src/integer_to_roman.py
[26]: https://leetcode.com/problems/roman-to-integer/
[27]: https://github.com/bluedazzle/leetcode_python/blob/master/src/roman_to_integer.py
[28]: https://leetcode.com/problems/longest-common-prefix/
[29]: https://github.com/bluedazzle/leetcode_python/blob/master/src/longest_common_prefix.py
[30]: https://leetcode.com/problems/3sum/
[31]: https://github.com/bluedazzle/leetcode_python/blob/master/src/3sum.py
[32]: http://blog.csdn.net/nanjunxiao/article/details/12524405
[33]: https://leetcode.com/problems/3sum-closest/
[34]: https://github.com/bluedazzle/leetcode_python/blob/master/src/3sum_closest.py
[35]: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
[36]: https://github.com/bluedazzle/leetcode_python/blob/master/src/letter_combinations_of_a_phone_number.py
[37]: https://leetcode.com/problems/4sum/
[38]: https://github.com/bluedazzle/leetcode_python/blob/master/src/4sum.py
[39]: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
[40]: https://github.com/bluedazzle/leetcode_python/blob/master/src/remove_nth_node_from_end_of_list.py
[41]: https://leetcode.com/problems/valid-parentheses/
[42]: https://github.com/bluedazzle/leetcode_python/blob/master/src/valid_parentheses.py
[43]: https://leetcode.com/problems/merge-two-sorted-lists/
[44]: https://github.com/bluedazzle/leetcode_python/blob/master/src/merge_two_sorted_lists.py
[45]: https://leetcode.com/problems/generate-parentheses/
[46]: https://github.com/bluedazzle/leetcode_python/blob/master/src/generate_parentheses.py
[47]: https://leetcode.com/problems/merge-k-sorted-lists/
[48]: https://github.com/bluedazzle/leetcode_python/blob/master/src/merge_k_sorted_lists.py
[49]: https://zh.wikipedia.org/wiki/%E5%88%86%E6%B2%BB%E6%B3%95
[50]: https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F
[51]: https://leetcode.com/problems/swap-nodes-in-pairs/
[52]: https://github.com/bluedazzle/leetcode_python/blob/master/src/swap_nodes_in_pairs.py
[53]: https://leetcode.com/problems/reverse-nodes-in-k-group/
[54]: https://github.com/bluedazzle/leetcode_python/blob/master/src/reverse_nodes_in_k-group.py
[55]: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
[56]: https://github.com/bluedazzle/leetcode_python/blob/master/src/remove_duplicates_from_sorted_array.py
[57]: https://leetcode.com/problems/remove-element
[58]: https://github.com/bluedazzle/leetcode_python/blob/master/src/remove_element.py
[59]: https://leetcode.com/problems/implement-strstr
[60]: https://github.com/bluedazzle/leetcode_python/blob/master/src/implement_strStr.py
[61]: https://leetcode.com/problems/divide-two-integers
[62]: https://github.com/bluedazzle/leetcode_python/blob/master/src/divide_two_integers.py