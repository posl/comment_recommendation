def f(a, b):
    if a % 4 == 0:
        return a
    elif a % 4 == 1:
        return 1
    elif a % 4 == 2:
        return a + 1
    elif a % 4 == 3:
        return 0
    if b % 4 == 0:
        return b
    elif b % 4 == 1:
        return 1
    elif b % 4 == 2:
        return b + 1
    elif b % 4 == 3:
        return 0
a, b = map(int, input().split())
ans = f(a - 1, b)
print(ans)
