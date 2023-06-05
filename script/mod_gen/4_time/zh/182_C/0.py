def solve(N):
    if N%3 == 0:
        return 0
    elif N%3 == 1:
        if 1 in nums:
            return 1
        elif 2 in nums and len(nums) >= 2:
            return 2
        else:
            return -1
    else:
        if 2 in nums:
            return 1
        elif 1 in nums and len(nums) >= 2:
            return 2
        else:
            return -1

if __name__ == '__main__':
    solve()