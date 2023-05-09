def main():
    n, q = map(int, input().split())
    x = [int(input()) for i in range(q)]
    a = list(range(1, n + 1))
    for i in range(q):
        a[x[i] - 1], a[x[i]] = a[x[i]], a[x[i] - 1]
    print(*a)
