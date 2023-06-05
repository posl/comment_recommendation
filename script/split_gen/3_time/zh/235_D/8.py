def solve(a, n):
    if n % a == 0:
        return -1
    ans = 1
    x = 1
    while True:
        x = (x * 10) % n
        ans += 1
        if x == 1:
            break
    return ans
a, n = map(int, input().split())
print(solve(a, n))
