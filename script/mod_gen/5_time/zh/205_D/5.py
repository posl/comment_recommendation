def solve(n, q, a, k):
    # write your code here
    # 二分查找
    def bisearch(target, nums):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) / 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        return low
    # 二分查找
    def bisearch2(target, nums):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) / 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        return low
    # 二分查找
    def bisearch3(target, nums):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) / 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        return low
    # 二分查找
    def bisearch4(target, nums):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) / 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        return low
    # 二分查找
    def bisearch5(target, nums):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) / 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        return low
    # 二分查找
    def bisearch6(target,

if __name__ == '__main__':
    solve()