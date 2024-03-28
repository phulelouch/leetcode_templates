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


  
  
