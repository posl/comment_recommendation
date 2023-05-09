def main():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(*a[:p-1], *a[q:r-1:-1], *a[s-1:p-1:-1], *a[r-1:], sep=' ')
