def main():
    nums = list(map(int, input().split()))
    nums.sort()
    if (nums[0] == nums[1] and nums[1] == nums[2] and nums[3] == nums[4]):
        print('Yes')
    elif (nums[0] == nums[1] and nums[2] == nums[3] and nums[3] == nums[4]):
        print('Yes')
    else:
        print('No')
