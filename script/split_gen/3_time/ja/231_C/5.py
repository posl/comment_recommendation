def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        ok = n
        ng = -1
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if a[mid] >= x[i]:
                ok = mid
            else:
                ng = mid
        print(n-ok)
