def solve(n):
    ans = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i*j > n:
                break
            for k in range(j, n+1):
                if i*j*k > n:
                    break
                ans += 1
    return ans
n = int(input())
print(solve(n))
