#1

def find_missing(nums):
    n = len(nums)
    expected = n * (n + 1) // 2
    actual = sum(nums)
    return actual - expected

numbers = [0, 1, 2, 4, 5]

print(find_missing(numbers))

#expected output = 3, right now output is -3

def find_missing(nums):
    n = len(nums)
    expected = n * (n + 1) // 2
    actual = sum(nums)
    return abs(actual-expected)

numbers = [0, 1, 2, 4, 5]

print(find_missing(numbers))

#applied abs() to remove the negative sign and get integral value

#2
# Problem
# Given an integer array nums,
# return an array where each element is the product of all the other elements except itself.

def product_except_self(nums):
    result = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(len(nums)):
        result[i] *= suffix
        suffix *= nums[i]

    return result


print(product_except_self([1, 2, 3, 4]))

#corrected:
#struggled a bit to find the fault

def product_except_self(nums):
    result = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


print(product_except_self([1, 2, 3, 4]))

