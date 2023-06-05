def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = a[0]
    for i in range(1, n):
        b[i] = max(b[i - 1], a[i])
    c = 0
    for i in range(n - 1, -1, -1):
        if b[i] > a[i]:
            c += b[i] - a[i]
        if b[i] <= a[i]:
            b[i] = a[i]
    print(c)
