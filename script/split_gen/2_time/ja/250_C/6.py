def main():
    N, Q = map(int, input().split())
    a = list(range(1, N + 1))
    for i in range(Q):
        x = int(input())
        idx = a.index(x)
        if idx == len(a) - 1:
            a[idx], a[idx - 1] = a[idx - 1], a[idx]
        else:
            a[idx], a[idx + 1] = a[idx + 1], a[idx]
    print(*a)
