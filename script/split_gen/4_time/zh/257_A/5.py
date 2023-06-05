def solve(n, x):
    for i in range(1, 27):
        if i * n >= x:
            return chr(64 + i)
n, x = map(int, input().split())
print(solve(n, x))
