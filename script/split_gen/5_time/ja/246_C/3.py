def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if k > 0:
            if a[i] >= x:
                ans += x
                k -= 1
            else:
                ans += a[i]
        else:
            ans += a[i]
    print(ans)
