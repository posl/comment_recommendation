def solve(x,k,d):
    if x < 0:
        x = -x
    if x//d >= k:
        return x - k*d
    else:
        return solve(x%d, k - x//d, d)
x, k, d = map(int, input().split())
print(solve(x,k,d))
