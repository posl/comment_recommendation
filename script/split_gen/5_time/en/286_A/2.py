def main():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if p <= i + 1 <= q or r <= i + 1 <= s:
            print(a[i], end=' ')
    for i in range(n):
        if not p <= i + 1 <= q and not r <= i + 1 <= s:
            print(a[i], end=' ')
    print()
