def solve(n):
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i * j > n:
                break
            ans += 1
    return ans
print(solve(int(input().strip())))
