# coding:utf-8
__author__ = 'annie'

# 给定一个整数数组nums，和一个目标值target,请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标
# 示例：给定nums = [2,7,11,15],target = 9
# 因为nums[0] + nums[1] = 2 + 7 = 9，所以返回[0,1]

def subscript(nums,target):
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                print(i,j)

nums = [2,7,11,15]
subscript(nums,9)



