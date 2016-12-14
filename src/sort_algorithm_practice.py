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
# time: 2016-12-02
#


class TestSort(object):
    func = None
    test_list = [[5, 3, 2, 4, 6, 1, 8, 4, 2],
                 [2, 1, 3, 4, 5, 6],
                 [1, 0, 0, 0, 0, 0, 2, 4]]
    results = [[1, 2, 2, 3, 4, 4, 5, 6, 8],
               [1, 2, 3, 4, 5, 6],
               [0, 0, 0, 0, 0, 1, 2, 4]]

    def __init__(self, func=None):
        self.func = func

    def run(self):
        print 'Starting test {0}:'.format(self.func.__name__)
        if not self.func:
            return None
        flag = True
        length = len(self.test_list)
        for i in xrange(length):
            res = self.func(self.test_list[i])
            try:
                assert res == self.results[i]
            except AssertionError:
                flag = False
                print 'Test({0}/{1}) failed!\r\nExpected:{2}\r\nActually:{3}'.format(i + 1, length, self.results[i],
                                                                                     res)
        if flag:
            print 'All tests({0}/{1}) passed'.format(length, length)
        return True

    def __call__(self, *args, **kwargs):
        func = args[0]
        if func:
            self.func = func
        self.run()


def bubble_sort(nums):
    length = len(nums) - 1
    for i in xrange(length):
        flag = True
        for j in xrange(length, i, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                flag = False
        if flag:
            break
    return nums


def select_sort(nums):
    length = len(nums)
    for i in xrange(length):
        min = i
        for j in xrange(i + 1, length):
            if nums[j] < nums[min]:
                min = j
        if i != min:
            nums[i], nums[min] = nums[min], nums[i]
    return nums


def insert_sort(nums):
    length = len(nums)
    for i in xrange(1, length):
        if nums[i] < nums[i - 1]:
            tmp = nums[i]
            position = i
            for j in xrange(i - 1, -1, -1):
                if tmp < nums[j]:
                    nums[j + 1] = nums[j]
                    position = j
                else:
                    break
            nums[position] = tmp
    return nums


def shell_sort(nums):
    length = len(nums)
    step = length // 3 + 1
    while step > 0:
        for i in xrange(step, length):
            tmp = nums[i]
            position = i
            for j in xrange(i - step, -1, -step):
                if tmp < nums[j]:
                    nums[position] = nums[j]
                    position = j
            nums[position] = tmp
        step //= 2
    return nums


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    def merge(left, right):
        res = []
        while left and right:
            if left[0] < right[0]:
                res.append(left[0])
                del left[0]
            else:
                res.append(right[0])
                del right[0]
        res.extend(left if left else right)
        return res

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    left = []
    privot_list = []
    right = []
    privot = nums[0]
    for i in nums:
        if i > privot:
            right.append(i)
        elif i < privot:
            left.append(i)
        else:
            privot_list.append(i)
    left = quick_sort(left)
    right = quick_sort(right)
    return left + privot_list + right


test = TestSort(bubble_sort)

test(quick_sort)

# print quick_sort([5, 3, 2, 4, 6, 1, 8, 4, 2])
