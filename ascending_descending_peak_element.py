
# Recursive function to find the peak element in a list
def findPeak(nums, left=None, right=None):
 
    # Initialize left and right

    # find the middle element. To avoid overflow, use mid = left + (right - left) / 2
    mid = (left + right) // 2
 
    # check if the middle element is greater than its neighbors
    if ((mid == 0 or nums[mid - 1] <= nums[mid]) and
            (mid == len(nums) - 1 or nums[mid + 1] <= nums[mid])):
        return mid
 
    # If the left neighbor of `mid` is greater than the middle element,
    # find the peak recursively in the left sublist
    if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
        return findPeak(nums, left, mid - 1)
 
    # If the right neighbor of `mid` is greater than the middle element,
    # find the peak recursively in the right sublist
    return findPeak(nums, mid + 1, right)
print(findPeak([1,2,3,4,5,6,2,1],0,7))
