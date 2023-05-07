def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    takahashi = 0
    aoki = 0
    while n > 0:
        for i in range(k):
            if n - a[i] >= 0:
                n -= a[i]
                takahashi += a[i]
                break
        for j in range(k):
            if n - a[j] >= 0:
                n -= a[j]
                aoki += a[j]
                break
    print(takahashi)
