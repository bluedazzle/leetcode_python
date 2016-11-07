# leetcode python solution

## Algorithms

#### 1. [Two Sum][1]: [Solution][2]
#### 2. [Add Two Numbers][3]: [Solution][4]
#### 3. [Longest Substring Without Repeating Characters][5]: [Solution][6]
#### 4. [Median of Two Sorted Arrays][7]: [Solution][8]
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
#### 11. [Container With Most Water][22]: [Solution][23] 
**tips: bf 做复杂度 O(n2) Python 会 TLE. 用两个游标分别从数组首位出发谁小谁移动, 纪录其中最大值, 复杂度 O(n)**
#### 12. [Integer to Roman][24]: [Solution][25]

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