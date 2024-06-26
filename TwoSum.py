"""Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
    and you may not use the same element twice.

You can return the answer in any order."""

def TwoSum(nums, target):
    for i in range(len(nums)):
        for j in range (i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Test Cases
Test = TwoSum([2,7,11,15], 9) # [0, 1]
print(Test)

print(TwoSum([3,2,4], 6)) # [1, 2]
