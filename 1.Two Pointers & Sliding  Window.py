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

#SLIDING WINDOW
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
