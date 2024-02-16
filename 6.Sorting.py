#1. Counting sort
#Ý tưởng: Đếm số lần xuất hiện của các phần tử.
#Giả sử nums = [1, 2, 3, 0, 6, 0, 1, 1, 3] c[0] = 2, c[1] = 3, c[2] = 1, c[3] = 2, c[6] = 1
# https://leetcode.com/problems/sort-colors/description/
def counting_sort(arr):
    # Find the maximum element in the array to know the range of the count array
    max_val = max(arr)
    
    # Initialize count array with all zeros
    count_arr = [0] * (max_val + 1)
    
    # Store the count of each element in count array
    for element in arr:
        count_arr[element] += 1

    print(count_arr)

    
    # Change count_arr[i] so that count_arr[i] now contains the actual
    # position of this element in the output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    
    print(count_arr)
    
    # Build the output character array
    output_arr = [0] * len(arr)
    for element in reversed(arr):
        output_arr[count_arr[element] - 1] = element
        count_arr[element] -= 1
    
    # Copy the output array to arr, so that arr now contains sorted characters
    for i in range(len(arr)):
        arr[i] = output_arr[i]

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1, 0]
counting_sort(arr)
print("Sorted array is:", arr)




###Radix sort

# 1. Sort dãy số theo thứ tự tăng dần của chữ số hàng đơn
# vị bằng 1 thuật toán sắp xếp ổn định.
# 2. Sort dãy số mới theo thứ tự tăng dần của chữ số hàng
# chục bằng 1 thuật toán sắp xếp ổn định.
# a. 2 phần tử có giá trị hàng chục bằng nhau thì
# phần tử nào có hàng đơn vị nhỏ hơn sẽ đứng
# trước.

# 3. Cứ làm như vậy cho đến chữ số hàng trăm, nghìn,...

# Dùng counting sort cho mỗi bước sắp xếp các chữ số kể
# trên.

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    
    # The output array elements that will have sorted arr
    output = [0] * n
    
    # Initialize count array as 0
    count = [0] * (10)
    
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i] // exp)
        count[(index) % 10] += 1
    
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp)
        output[count[(index) % 10] - 1] = arr[i]
        count[(index) % 10] -= 1
        i -= 1
    
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)
    
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Sorted array is:", arr)



def radix_sort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)
    
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Sorted array is:", arr)



#2. Divide and Conquer
#https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def findKthLargest(self, nums, k):
        return self.findKthElement(nums, len(nums) - k + 1)

    """
        Template: Find the kth smallest element in the array
        -   Pick random pivot
        -   Divide and conquer
        left_pivots < pivots < right_pivots
        ----------------------------------------
            < pivot  |     pivot     | > pivot
        --------->kth
        ------------------->kth
        -------------------------------->kth
    """
    def findKthElement(self, nums, k):
        # Base case
        if len(nums) == 1:
            return nums[0]

        pivot = nums[len(nums) // 2]
        
        left_pivots = [x for x in nums if x < pivot]
        pivots = [x for x in nums if x == pivot]
        right_pivots = [x for x in nums if x > pivot]

        # If kth largest element belongs to left_pivots
        if k <= len(left_pivots) :
            return self.findKthElement(left_pivots, k)
        
        elif k <= len(left_pivots) + len(pivots):
            return pivot

        else:
            # k also change how big it is in the right cause all the bigger than pivot is already remove 
            # so  k - len(left_pivots) - len(pivots)
            return self.findKthElement(right_pivots, k - len(left_pivots) - len(pivots))


#https://leetcode.com/problems/diameter-of-binary-tree/description/
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.diameter = 0

    def counting(root):
        if not root:
            return 0
        count_left = counting(root.left)
        count_right = counting(root.right)
        #print(count_left,count_right)
        self.diameter = max(self.diameter, count_left+count_right)
        return max(count_left,count_right) + 1
    
    counting(root)
    return self.diameter

