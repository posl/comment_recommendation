def solve(n, a):
    if 0 in a:
        return 0
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10**18:
            return -1
    return ans
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
