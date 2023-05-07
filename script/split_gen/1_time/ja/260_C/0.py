def main():
    n, x, y = map(int, input().split())
    if n == 1:
        print(0)
        return
    if n == 2:
        print(x)
        return
    if n == 3:
        print(x + y)
        return
    a = [0] * (n + 1)
    a[1] = 0
    a[2] = x
    a[3] = x + y
    for i in range(4, n + 1):
        a[i] = min(a[i - 1] + x, a[i - 2] + y)
    print(a[n])
