def solve():
    n,x,y = map(int,input().split())
    nums = list(map(int,input().split()))
    if x < min(nums) or x > max(nums) or y < min(nums) or y > max(nums):
        print("No")
        return
    nums.append(0)
    nums.sort()
    for i in range(n):
        for j in range(i+1,n+1):
            if nums[i] + nums[j] == y:
                if nums[i] == 0 and nums[j] == 0:
                    print("Yes")
                    return
                if nums[i] == 0 and nums[j] == x:
                    print("Yes")
                    return
                if nums[i] == x and nums[j] == 0:
                    print("Yes")
                    return
                if nums[i] == x and nums[j] == x:
                    print("Yes")
                    return
    print("No")
solve()
