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