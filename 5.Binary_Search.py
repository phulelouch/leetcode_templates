# Binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m -1
            else:
                l = m +1
        return -1


class Solution:
        def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            if not matrix:
                return False
            
            m, n = len(matrix), len(matrix[0])
            left, right = 0, m * n - 1

            while left <= right:
                mid = (left + right) // 2
                
                mid_row, mid_col = divmod(mid, n)
                print(mid, n)
                print(mid_row, mid_col)

                if matrix[mid_row][mid_col] == target:
                    return True
                elif matrix[mid_row][mid_col] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return False

        
    
# Binary search with situation:
#Step 1: make an not efficency method with for that advance left:

def arrangeCoins(self, n: int) -> int:
        if n==1 or n==2:
            return 1
        if n==3:
            return 2
        for i in range(n):
            if n < i*(i+1)/2:
                return i-1

#Step 2: based on condition to advance right or left:
            # dựa vào muốn tìm lớn hơn hay trong khoảng để bỏ ans = mid vào left hay right 
            # Nếu cần tìm để điều kiện trong khoảng (nhỏ hơn) thì bỏ vào right 
            # cần tìm để diều khiện lớn hơn thì bỏ vào left

def arrangeCoins(self, n: int) -> int:
        if n==1 or n==2:
            return 1
        if n==3:
            return 2

        left = 0
        right = n-1
        ans = 0
        while left <= right:
            m = (left+right)//2
            if n < m*(m+1)/2 :
                right = m-1
            else:
                ans = m
                left = m+1
                
        return ans



# bisect_left (sortedArr, target, lo=0,
# hi=len(sortedArr) )
# Trả về chỉ số vị trí của phần tử đầu tiên lớn hơn hoặc bằng target trong đoạn [lo, hi).
# Đó cũng chính là vị trí chèn trai.

def bisect_left(nums, target):
    left = 0
    right = len(nums) - 1
    ans = len(nums)
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            ans = mid  # update the best result so far
            right = mid - 1  # search better result on the left side
        else:
            left = mid + 1  # search result on the right side
    return ans


# bisect_right (sortedArr, target, lo=0,
# hi=len(sortedArr) )
# Trả về chỉ số vị trí của phần tử đầu tiên lớn hơn target trong đoạn [lo, hi).
# Đó cũng chính là vị trí chèn phải.

def bisect_right(nums, target):
    left = 0
    right = len(nums) - 1
    ans = len(nums)
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            ans = mid  # update the best result so far
            right = mid - 1  # search better result on the left side
        else:
            left = mid + 1  # search result on the right side
    return ans


def searchRange(nums, target):
        n=len(nums)
        if n == 0:
            return [-1,-1]
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)-1
        if left == n or right == n:
            return [-1,-1]
        if nums[left] == target and nums[right] == target :
            return [left, right]
        else:
            return [-1,-1]
        

nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums, target))

# Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

# Notice that all the heaters follow your radius standard, and the warm radius will the same.

# Example 2:

# Input: houses = [1,2,3,4], heaters = [1,4]
# Output: 1
# Explanation: The two heaters were placed at positions 1 and 4. We need to use a radius 1 standard, then all the houses can be warmed.


def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # [1,2,3]
        # [2]
        # []
        heaters.sort()

        list_min_radius = []
        for house in houses:
            left = bisect.bisect_right(heaters, house)-1
            right = bisect.bisect_right(heaters, house)
            if right == len(heaters):
                right = len(heaters) -1
            if left == -1:
                left = 0
            print(left,right)
            iLeft = abs(heaters[left] - house)
            iRight = abs(heaters[right] - house)
            min_radius = min(iLeft, iRight)
            print(min_radius)
            list_min_radius.append(min_radius)
        print(list_min_radius)
        
        return max(list_min_radius)




# The frequency of an element is the number of times it occurs in an array.
# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.
# Return the maximum possible frequency of an element after performing at most k operations.
# Example 1:

# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4]. 4 has a frequency of 3.

def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        def find_max_freq_of_num(i):
            left = 0
            right = len(nums)
            result = i
            while left <= right:
                mid = (left+right)//2
                #print(mid, right,nums[i]*(i - mid + 1),sum(nums[mid:i+1]))
                op_need = nums[i]*(i- mid + 1) - sum(nums[mid:i+1])
                if op_need <= k:
                    result = mid
                    right = mid -1
                else:
                    left = mid + 1
                   
            return result

        max_freq = 0
        for i in range(len(nums)):
            j=find_max_freq_of_num(i)
            max_freq = max(max_freq, i-j+1)
        return max_freq
        
#totalBouquests
class Solution:


    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def totalBouquests(day):
            count =0
            bCanMake = 0
            for i in bloomDay:
                if i <= day:
                    count+=1
                else:
                    bCanMake += count // k
                    count=0
            bCanMake += count // k
            return bCanMake 
        
        bloomDaySort = bloomDay.copy()
        bloomDaySort.sort()
            
        # for j in bloomDaySort:
        #     if totalBouquests(j) >= m:
        #         return j
        # return -1

        left = min(bloomDay)
        right = max(bloomDay)
        ans = -1
        while left <= right:
            mid = (left+right) // 2
            if totalBouquests(mid) >= m: 
                ans = mid
                right = mid-1
            else:
                left = mid +1

        return ans
        

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def countDays(w):
            count = 0
            numWeights = 0 
            for i in weights:
                if numWeights+i <= w:
                    numWeights += i
                else:
                    count += 1
                    numWeights = i
            count +=1
                
            return count

        
        left = max(weights)
        right = sum(weights)
        ans = 0
        while left <= right:
            mid = (left+right)//2
            if countDays(mid) <= days:
                right = mid -1
                ans = mid
            else:
                left = mid +1
                
        return ans


        # for i in range(max(weights),totalWeight+1):
        #     print(f"Weight: {i}")
        #     if countDays(i) <= days:
        #         return i
        # return 0

# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence
# .

 
#Longest increasing subsequence
# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
        

def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            if not sub or num > sub[-1]:
                sub.append(num)
            else:
                i = bisect.bisect_left(sub, num)
                sub[i] = num
        print(sub)
        return len(sub)


  
# Russian Doll Envelopes

# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

# One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

# Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

# Note: You cannot rotate an envelope.

 

# Example 1:

# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
# Example 2:

# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1

def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

    def lengthOfLIS(nums):
        sub = []
        for num in nums:
            if not sub or num > sub[-1]:
                sub.append(num)
            else:
                i = bisect.bisect_left(sub, num)
                sub[i] = num
        print(sub)
        return len(sub)

    envelopes.sort(key=lambda x:[x[0], -x[1]])
    print(envelopes)

    
    arr = [h for _,h in envelopes]
    print(arr)
    return lengthOfLIS(arr)
        

