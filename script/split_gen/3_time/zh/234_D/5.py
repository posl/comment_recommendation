def solve(n,k,nums):
    # 从中间开始比较，找到第k大的数
    # 从中间开始比较，找到第k大的数
    def findKth(nums,k):
        if len(nums)==1:
            return nums[0]
        mid = len(nums)//2
        left = [i for i in nums if i<nums[mid]]
        right = [i for i in nums if i>nums[mid]]
        if len(right)>=k:
            return findKth(right,k)
        elif len(right)==k-1:
            return nums[mid]
        else:
            return findKth(left,k-len(right)-1)
    for i in range(k,n+1):
        print(findKth(nums[:i],k))
