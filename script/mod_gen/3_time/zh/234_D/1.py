def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]

if __name__ == '__main__':
    findKthLargest()