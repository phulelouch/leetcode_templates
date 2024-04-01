Shifted Array Search
A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and you don’t have a pre-shifted copy of it. For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.

Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in shiftArr. If num isn’t in shiftArr, return -1. Assume that the offset can be any value between 0 and arr.length - 1.

Explain your solution and analyze its time and space complexities.

Example:

input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
                                                 # outcome of shifting
                                                 # [2, 4, 5, 9, 12, 17]
                                                 # three times to the left

output: 3 # since it’s the index of 2 in arr
Constraints:

[time limit] 5000ms
[input] array.integer arr
[input] integer num
[output] integer



def index_equals_value_search(arr):
  #for i in arr:
  #  if arr[i] == i:
  #    return arr[i]
    
  #return -1
  #O(logN+1) => if N is close to inf => N
  # log(N) => in each iteration u are dividing the input by 2
  
  
  L = 0
  R = len(arr) - 1
  ans = 99999999
  
  while L <= R:
    M = (L+R)//2
    if arr[M] == M:
      ans = min(ans, M)
      R = M - 1
    elif arr[M] > M:
      R = M - 1
    else:
      L = M + 1
      
  return ans if ans != 99999999 else -1
  
  
test_arr = [-6,41,2,3,4,5]
test_arr2 = [0,1,2,3,4,5]
print(index_equals_value_search(test_arr))


#original
function indexEqualsValueSearch(arr):
    start = 0
    end = arr.length - 1

    while (start <= end):
        i = round((start+end)/2)
        if (arr[i] - i < 0):
            start = i+1
        else if (arr[i] - i == 0) and ((i == 0) or (arr[i-1] - (i-1) < 0)):
            return i
        else:
            end = i-1

    return -1




ans = float('inf')  
def get_cheapest_cost(root):
  
  if root.children == []: # sepcial situtation
    return root.cost
  
  
  def dfs(node, total):
    global ans
    
    if node.children == []: #based case for dfs
      ans = min(ans, total) # total = 0
    
    for child in node.children: # 
      dfs(child, total+child.cost)
      
      
  dfs(root, root.cost)
  return ans

my github phulelouch, cheers
shivam0rawat0 , cheeers
      
    
    
    
########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None
    
root = Node(0)
child11 = Node(1)
child12 = Node(5)
child13 = Node(6)

child21 = Node(1)
child11.children.append(child21)

root.children.append(child11)
root.children.append(child12)
root.children.append(child13)

print(get_cheapest_cost(root))





# QUESTION
# Time Planner
# Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies the duration requirement, return an empty array.

# Time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

# Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two. The first epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot. The input variable dur is a positive integer that represents the duration of a meeting in seconds. The output is also a pair represented by an epoch array of size two.

# In your implementation assume that the time slots in a person’s availability are disjointed, i.e, time slots in a person’s availability don’t overlap. Further assume that the slots are sorted by slots’ start time.

# Implement an efficient solution and analyze its time and space complexities.

# Examples:

# input:  slotsA = [[10, 50], [60, 120], [140, 210]]
#         slotsB = [[0, 15], [60, 70]]
#         dur = 8
# output: [60, 68]

# input:  slotsA = [[10, 50], [60, 120], [140, 210]]
#         slotsB = [[0, 15], [60, 70]]
#         dur = 12
# output: [] # since there is no common slot whose duration is 12
# Constraints:

# [time limit] 5000ms

# [input] array.array.integer slotsA

# 1 ≤ slotsA.length ≤ 100
# slotsA[i].length = 2
# [input] array.array.integer slotsB

# 1 ≤ slotsB.length ≤ 100
# slotsB[i].length = 2
# [input] integer

# [output] array.integer

#I found a LeetCode problem that matches your description: "1229. Meeting Scheduler". It involves finding the earliest time slot that fits the meeting duration for two people given their available time slots. If no common time slot satisfies the duration requirement, it returns an empty array. The problem emphasizes sorting the slots and using two pointers to find the intersection of the available times that meet or exceed the specified duration. For more details, you can visit the problem page on LeetCode via this link.

def time_planner(slotsA, slotsB, dur):
    lenA = len(slotsA)
    lenB = len(slotsB)
    i = 0
    j = 0
    while i < lenA and j < lenB:
        start = max(slotsA[i][0], slotsB[j][0])
        end = min(slotsA[i][1], slotsB[j][1])
        if end - start >= dur:
            return [start, start+dur]
        if slotsA[i][1] < slotsB[j][1]: # if A ends before B
            i+=1
        else: #if B ends before A
            j+=1
    return []

print(time_planner(slotsA, slotsB, dur))
  
