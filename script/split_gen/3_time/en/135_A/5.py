def solve(a, b):
    if a == b:
        return 'IMPOSSIBLE'
    return str((a + b) // 2)
a, b = map(int, input().split())
print(solve(a, b))
