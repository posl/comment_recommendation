def main():
    n, q = map(int, input().split())
    x = [int(input()) for _ in range(q)]
    a = [i for i in range(1, n+1)]
    for i in range(q):
        a[i], a[i+1] = a[i+1], a[i]
        if a[i] == x[i]:
            a[i], a[i+1] = a[i+1], a[i]
    print(*a)
