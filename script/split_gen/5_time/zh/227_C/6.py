def solve(n):
    ans = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            for k in range(j, n+1):
                if i*j*k <= n:
                    if i == j and j == k:
                        ans += 1
                    elif i == j or j == k:
                        ans += 3
                    else:
                        ans += 6
                else:
                    break
    return ans
n = int(input())
print(solve(n))
