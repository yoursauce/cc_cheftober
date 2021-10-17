# This is an iterative implementation of binary search in python
def binarySearch(arr, l, r, x):
 
    while l <= r:
 
        mid = l + (r - l) // 2;
         
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
 
        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
 
        # If x is smaller, ignore right half
        else:
            r = mid - 1
     
#If value not found in list
    return -1
 
# Driver Code


arr = list(map(int, input().split()))
x= int(input())
 
# Function call
result = binarySearch(arr, 0, len(arr)-1, x)
 
if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")