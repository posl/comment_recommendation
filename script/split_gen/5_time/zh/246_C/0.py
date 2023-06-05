def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if k > 0:
            ans += max(a[i] - x, 0)
            k -= 1
        else:
            ans += a[i]
    print(ans)
