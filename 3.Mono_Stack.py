# Monostack find bigger on the left

def skyline_stack(nums):
    n = len(nums)
    stack = []
    result = [-1] * n  # Initialize the result list with -1s
    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()  # pop from stack if current number is greater than stack's top
        if stack:
            result[i] = stack[-1]  # peek the last element of the stack
        else:
            result[i] = -1  # if stack is empty, result is -1
        stack.append(i)  # push the current index onto the stack
    return result
    
#1. https://leetcode.com/problems/next-greater-element-ii/
#reversed find bigger on right
def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        result = [-1] * n  # Initialize the result list with -1s
        nums = nums+nums #remove this if wanted for not circle
        
        for i in reversed(range(n*2)):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()  # pop from stack if current number is greater than stack's top
            if i <n:
                if stack:
                        result[i] = nums[stack[-1]]  # peek the last element of the stack
                else:
                    result[i] = -1  # if stack is empty, result is -1
            
            stack.append(i)  # push the current index onto the stack
        
        return result

#2. https://leetcode.com/problems/maximum-subarray-min-product/

def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        #find left boundary
        stack = []
        left = [-1] * n  # Initialize the result list with -1s
        
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()  # pop from stack if current number is greater than stack's top
            if stack:
                left[i] = stack[-1]  # peek the last element of the stack
            else:
                left[i] = -1  # if stack is empty, result is -1
            stack.append(i)  # push the current index onto the stack

        #find right boundary 
        stack = []
        right = [-1] * n  # Initialize the result list with -1s 
        for i in reversed(range(n)):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()  # pop from stack if current number is greater than stack's top
            if stack:
                right[i] = stack[-1]  # peek the last element of the stack
            else:
                right[i] = -1  # if stack is empty, result is -1
            stack.append(i)  # push the current index onto the stack

        maxium = int(0)
        #print(left, right)
        for i in range(n):
            if right[i]==-1:
                right[i]=n
            total = nums[i]*sum(nums[left[i]+1:right[i]])
            maxium = max(total, maxium)
            # print(nums[i])
            # print(left[i]+1,right[i])
            # print(total)
        return maxium % 1_000_000_007

## Queue with max API using queues
# Queue with max API

# Hãy viết class MaxQueue có các API sau:
# 1. void enqueue(int x): Thêm số x vào cuối queue.
# 2. int dequeue(): Xóa phần tử ở đầu queue và return ra phần tử đó.
# 3. int getMax(): Trả về giá trị lớn nhất trong queue hiện tại.
# VD:
# enqueue(4);
# enqueue(2);
# enqueue(3);
# getMax(); //return 4
# dequeue(); //return 4
# getMax(); //return 3

entryQueue = []
candidateQueue = []

def enqueue(x):
    entryQueue.append(x)  # push into back of queue
    while candidateQueue and candidateQueue[-1] < x:
        candidateQueue.pop()
    candidateQueue.append(x)
    
def dequeue():
    if not entryQueue:
        return None  # or raise an exception if you prefer
    removedValue = entryQueue.pop(0)  # pop from front of queue
    if candidateQueue and removedValue == candidateQueue[0]:
        candidateQueue.pop(0)
    return removedValue
    
def getMax():
    return candidateQueue[0] if candidateQueue else None


# Arithmetic expressions problem

# Bài toán cơ bản: Một biểu thức được mô tả dưới dạng 1 dãy các string là
# các toán tử và toán hạng. Hãy tính ra kết quả của biểu thức đó.
# Biểu thức chỉ có phép cộng, trừ và nhân.
# Ví dụ : input =[“3”, “+”, “2”, “*”, “3”, “-”, “4”] ==> output: 5
# Giải thích: Biểu thức là 3 + 2 * 3 - 4, kết quả là 5.

def calculate(input_expression):
    stack = []
    for x in input_expression:
        if x in ["+", "-", "*", "/"]:  # If it's an operator
            stack.append(x)
        else:  # If it's a number
            operator = stack[-1] if stack else None
            if operator in ["*"]:
                stack.pop()  # Remove the operator from the stack
                y = stack.pop()  # Get the first operand
                temp_result = y * int(x)
                stack.append(temp_result)  # Add the result to the stack
            elif operator in [ "/"]:
                stack.pop()  # Remove the operator from the stack
                y = stack.pop()  # Get the first operand
                temp_result = y / int(x)
                stack.append(temp_result)  # Add the result to the stack

            elif x in ["+", "-"]:
                stack.append(x) # x is +, -
            else:
                stack.append(int(x)) # x is number
    
    r = stack.pop(0)
    while len(stack)!=0:
        operator = stack.pop(0)
        num = stack.pop(0)
        if operator =="+":
            r += num
        else:
            r -= num



    return r  # If the stack is empty, return 0

# Example usage:
result = calculate(["3", "*", "5", "+", "2", "-","3","*","2","/","2"]) 
print(result)  # Expected output: 15+2-3*2/2

#also Queue template
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    # Implementing this with dummy nodes would be easier!
    def __init__(self):
        self.left = self.right = None
    
    def enqueue(self, val):
        newNode = ListNode(val)

        # Queue is non-empty
        if self.right:
            self.right.next = newNode
            self.right = self.right.next
        # Queue is empty
        else:
            self.left = self.right = newNode

    def dequeue(self):
        # Queue is empty
        if not self.left:
            return None
        
        # Remove left node and return value
        val = self.left.val
        self.left = self.left.next
        if not self.left:
            self.right = None
        return val

    def print(self):
        cur = self.left
        while cur:
            print(cur.val, ' -> ', end ="")
            cur = cur.next
        print() # new line

