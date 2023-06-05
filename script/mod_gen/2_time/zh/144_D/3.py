def solve(n):
    ans = 1
    while ans * ans < n:
        ans += 1
    if ans * ans == n:
        return 2 * ans - 2
    elif (ans - 1) * ans < n <= (ans - 1) * ans + ans:
        return 2 * ans - 1
    else:
        return 2 * ans
n = int(input())
print(solve(n))
