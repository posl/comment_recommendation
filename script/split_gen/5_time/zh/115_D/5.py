def count_burger(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + count_burger(n - 1, (1 << n) - 2):
        return count_burger(n - 1, x - 1)
    else:
        return 1 + count_burger(n - 1, x - 2 - count_burger(n - 1, (1 << n) - 2))
n, x = map(int, input().split())
print(count_burger(n, x))
