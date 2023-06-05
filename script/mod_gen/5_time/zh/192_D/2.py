def solve(x, m):
    d = int(max(x))
    ans = 0
    for i in range(d + 1, 10):
        if int(x, i) <= m:
            ans += 1
    return ans
x = input()
m = int(input())
print(solve(x, m))
