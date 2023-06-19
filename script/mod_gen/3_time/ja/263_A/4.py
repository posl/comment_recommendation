def main():
    nums = list(map(int, input().split()))
    if len(set(nums)) == 2:
        if nums.count(nums[0]) == 2 or nums.count(nums[0]) == 3:
            print("Yes")
            return
    print("No")
main()
