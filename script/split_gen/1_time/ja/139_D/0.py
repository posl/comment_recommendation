def calc(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return n * (n - 1) // 2
n = int(input())
print(calc(n))
