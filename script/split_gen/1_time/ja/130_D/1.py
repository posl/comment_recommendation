def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += a[j]
            if s >= k:
                ans += n - j
                break
    print(ans)
