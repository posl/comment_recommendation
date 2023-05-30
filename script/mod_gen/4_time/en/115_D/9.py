def burger(n, x):
    if n == 0: return 1
    mid = (2 ** (n + 2)) - 3
    if x == 1: return 0
    elif x <= mid: return burger(n - 1, x - 1)
    elif x == mid + 1: return (2 ** (n + 1)) - 1
    elif x <= (2 ** (n + 1)) + mid - 1: return (2 ** n) + burger(n - 1, x - mid - 2)
    else: return (2 ** (n + 1)) - 1
n, x = map(int, input().split())
print(burger(n, x))
