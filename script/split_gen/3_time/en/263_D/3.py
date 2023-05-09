def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i < n // 2:
            ans += min(l, a[i])
        else:
            ans += min(r, a[i])
    print(ans)
