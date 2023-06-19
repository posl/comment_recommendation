def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if m == 0:
        print(1)
        return
    if n == m:
        print(0)
        return
    d = []
    for i in range(1, m):
        d.append(a[i] - a[i - 1] - 1)
    d.sort()
    s = sum(d[:m - n])
    print(s + 1)
