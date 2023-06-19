def solve(n, a, b):
    if n<=a:
        return n
    else:
        return a + (n-a)%b
n, a, b = map(int, input().split())
print(solve(n, a, b))
