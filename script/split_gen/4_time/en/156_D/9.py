def calc(n, a, b):
    if a > b:
        a, b = b, a
    if a + 1 == b:
        return n - 2
    else:
        return (n - 2) * (n - 2) % 1000000007
n, a, b = map(int, input().split())
print(calc(n, a, b))
