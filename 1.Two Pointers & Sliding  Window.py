# 1. Bài toán cơ bản

# Cho dãy n số nguyên arr được sắp xếp theo thứ tự tăng dần và một số nguyên target. Hỏi có tồn tại 2
# phần tử trong mảng sao cho tổng của chúng bằng target. Nếu tồn tại trả về chỉ số vị trí 2 phần tử đó,
# nếu không tồn tại trả về [-1, -1].
# Ví dụ:
# Input: arr = [1, 2, 4, 7, 9, 10], target = 6
# Output: [1, 2]

# Giới hạn dữ liệu:
# ● 1 <= nums.length <= 10^5
# ● -10^9 <= nums[i], target <= 10^9


#ALSO TEMPLATE FOR 2 POINTERS
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    right = int(len(numbers))-1
    left = 0
    while left<right:
        if numbers[left] + numbers[right] == target:
            return [left+1, right+1]
            break
        elif numbers[left] + numbers[right] > target:
            right -= 1
        elif numbers[left] + numbers[right] < target:
            left += 1


#TEMPLATE FOR 3 POINTERS
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    for i in range(0,len(nums)-2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        left = i+1
        right = len(nums)-1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total > 0:
                right -=1
            elif total < 0:
                left += 1
            else:
                triplet = [ nums[i], nums[left], nums[right]]
                result.append(triplet)
                while left < right and nums[left] == triplet[1]:
                    left +=1
                while left < right and nums[right] == triplet[2]:
                    right -=1
    return result
    


def triangleNumber(self, nums: List[int]) -> int:
    nums.sort()
    result = 0
    n = len(nums)
    for i in reversed(range(n)):
        left = 0
        right = i-1
        while left < right:
            total = nums[left] + nums[right]
            if total>nums[i]:
                result += right -left
                right -=1
            else:
                left +=1
    return result
    

def judgeSquareSum(self, c: int) -> bool:
    j = int(math.sqrt(c))
    i = 0
    while i<=j:
        if i**2 + j**2 == c:
            return True
            break
        elif i**2 + j**2 > c:
            j -= 1
        elif i**2 + j**2 < c:
            i += 1

    return False

#https://leetcode.com/problems/container-with-most-water/
def maxArea(self, height: List[int]) -> int:
    n = len(height)
    max_water = 0
    L= 0
    R = (n-1)
    Lismin = True
    nobigger = False
    while L<R:
        
        if height[L] <= height [R]:
            Lismin = True
            min_val = height[L]
        else:
            min_val = height[R]
            Lismin = False

        max_water = max(max_water, min_val*(R-L))
        #print(L,R,max_water)

        if Lismin:
            original_height = height[L]
            L += 1
            while L < R and height[L] <= original_height:
                L += 1
        
        else:
            original_height = height[R]
            R -= 1
            while L < R and height[R] <= original_height:
                R -= 1
        
    return max_water

#SLIDING WINDOW FIX SIZE
#https://leetcode.com/problems/contains-duplicate-ii/

def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    n=len(nums)
    L=0
    window=set()

    for R in range(n):
        if R-L > k:
            window.remove(nums[L])
            L+=1
        if nums[R] in window:
            return True

        window.add(nums[R])
    
    return False


#https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        n=len(nums)
        L=0
        count=0
        window_sum=0
        
        for R in range(n):
            window_sum += nums[R]
            if R - L + 1 == k:
                if window_sum / k >= threshold:
                    count += 1
                window_sum -= nums[L]
                L += 1
        
        return count

def slidingWindowTemplate(nums: List[int], k: int) -> int:  # Change return type based on the problem
    n = len(nums)
    L = 0  # Left edge of the sliding window
    result = 0  # Change based on what you need to compute
    window_computation = 0  # This could be a sum, a product, a set, etc., based on the problem

    for R in range(n):  # R is the right edge of the sliding window
        # Update window_computation with the new element added to the window
        window_computation += ...  # Change this based on the problem

        # Check if the window is of the desired size k
        if R - L + 1 == k:
            # Compute result using window_computation
            # This could involve checking a condition or updating a maximum/minimum, etc.
            result += ...  # Change this based on the problem

            # Remove the element at the left edge of the window from window_computation
            window_computation -= nums[L]  # Change this based on the problem
            L += 1  # Slide the window to the right by one element

    return result


#SLIDING WINDOW DYNAMIC SIZE
#https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstringWithoutRepeating(self, nums: str) -> int:
    length = 0
    L = 0
    window=set()

    for R in range(len(nums)):
        
        while nums[R] in window:
            window.remove(nums[L])
            print(f"Remove {L}")
            L += 1
        length = max(length, R - L + 1)
        window.add(nums[R])
    return length

def lengthOfLongestRepeatingSubstring(s: str) -> int:
    if not s:
        return 0

    length = 0
    L = 0

    for R in range(1, len(s)):
        # If the current character is different from the previous one,
        # update the left pointer and calculate the length.
        if s[R] != s[R - 1]:
            L = R
        length = max(length, R - L + 1)

    return length

#https://leetcode.com/problems/longest-repeating-character-replacement/
def characterReplacement(self, s: str, k: int) -> int:
            if not s:
                return 0

            length = 0
            L = 0
            max_f = 0
            count = {}

            for R in range(0, len(s)):
                count[s[R]] = count.get(s[R],0) +1
                max_f = max(max_f, count[s[R]])
                if R-L+1 - max_f > k:
                    count[s[L]] -=1
                    L +=1
                   
                length = max(length, R - L + 1)

            return length


#https://leetcode.com/problems/minimum-size-subarray-sum/
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    l = 0
    min_len = 999999999
    current_sum = 0

    for r in range(len(nums)):
        current_sum += nums[r]

        while current_sum >= target:
            min_len = min(min_len, r - l + 1)
            current_sum -= nums[l]
            l += 1

    return min_len if min_len != 999999999 else 0


#https://leetcode.com/problems/minimum-window-substring/
def minWindow(self, s: str, t: str) -> str:
    if len(s)<len(t):
        return ""
    if s==t:
        return s
    if len(t)==1:
        if t in s:
            return t
        else:
            return ""
    
        
    count = {char: 0 for char in t}
    true_count = Counter(t)
    length = 999999999
    L = 0
    minL, minR = 0,0
    def check(c, tc):
        return all(c.get(key) > 0 and c.get(key) >= tc.get(key) for key in c.keys())


    for R in range(0, len(s)):
        if s[R] in t:
            count[s[R]] = count.get(s[R],0) +1
        while check(count, true_count):
            if length > R-L+1:
                length = R-L+1
                minL, minR = L,R
            if count.get(s[L]):
                    count[s[L]] = count.get(s[L]) - 1
            L+=1
        
        
    if minL ==0 and minR==0 and length == 999999999:
        return ""

    return s[minL:minR+1] 

