def solve(a,b,k):
    if a >= b:
        return 0
    if k == 1:
        return b - a
    ans = 0
    while a < b:
        a *= k
        ans += 1
    return ans
a,b,k = map(int,input().split())
print(solve(a,b,k))
