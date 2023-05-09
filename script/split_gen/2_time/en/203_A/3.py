def main():
    nums = input().split()
    nums = [int(x) for x in nums]
    if nums[0] == nums[1]:
        print(nums[2])
    elif nums[0] == nums[2]:
        print(nums[1])
    elif nums[1] == nums[2]:
        print(nums[0])
    else:
        print(0)
