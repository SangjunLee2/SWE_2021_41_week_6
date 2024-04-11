from typing import List

def twoSum(nums: List[int], target: int):
    for idx, num in enumerate(nums):
        comp=target-num
        if(comp in nums[idx+1:]): 
            idx2=1+idx+nums[idx+1:].index(comp)
            return [idx,idx2]

