#Subsets - Distinct elements
# Time: O(n * 2^n), Space: O(n)
def subsetsWithoutDuplicates(nums):
    subsets, curSet = [], []
    helper(0, nums, curSet, subsets)
    return subsets

def helper(i, nums, curSet, subsets):
    if i >= len(nums):
        subsets.append(curSet.copy())
        return
    
    # decision to include nums[i]
    curSet.append(nums[i])
    helper(i + 1, nums, curSet, subsets)
    curSet.pop()

    # decision NOT to include nums[i]
    helper(i + 1, nums, curSet, subsets)



#Subsets - non-distinct elements
# Time: O(n * 2^n), Space: O(n)
def subsetsWithDuplicates(nums):
    nums.sort()
    subsets, curSet = [], []
    helper2(0, nums, curSet, subsets)
    return subsets

def helper2(i, nums, curSet, subsets):
    if i >= len(nums):
        subsets.append(curSet.copy())
        return
    
    # decision to include nums[i]
    curSet.append(nums[i])
    helper2(i + 1, nums, curSet, subsets)
    curSet.pop()

    # decision NOT to include nums[i]
    while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        i += 1
    helper2(i + 1, nums, curSet, subsets)





def subsetsWithk(self, nums: List[int], k: int) -> List[List[int]]:
    combs = []
    n = len(nums)
    
    def helper2(i, curComb, combs, n, k):
        if len(curComb) == k:
            combs.append(curComb.copy())
            return
        if i > n:
            return
    
        for j in range(i, n):
            curComb.append(nums[j])
            helper2(j + 1, curComb, combs, n, k)
            curComb.pop()
    
    
    helper2(0, [], combs, n, k)
    return combs
