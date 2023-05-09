def getMinSteps(n, m):
    if n == 1:
        return 0
    if m == 1:
        return n - 1
    if m == 2:
        return 2 if n == 2 else 3
    if n == 2:
        return 2
    if n == 3:
        return 4
    return 4 + (n - 4) * 2
n, m = map(int, input().split())
print(getMinSteps(n, m))
