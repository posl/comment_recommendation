def calc(n):
    if n == 0:
        return 0
    if n == 1:
        return 2
    if n == 2:
        return 20
    return calc(n-1)*10 + 2
K = int(input())
print(calc(K))
