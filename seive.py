#!/usr/bin/env python3

nums = list(range(2,44))
#print(nums)

def check_num(num, lst: list):
    i = 0
    while i < len(lst):
        if lst[i] % num == 0 and lst[i] != num:
            lst.pop(i)
        else:
            i += 1

i = 0
while i < len(nums):
    check_num(nums[i], nums)
    i += 1

for i in nums:
    print(i)
