def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(n-1):
        if a[i] == a[i+1]:
            continue
        if k >= a[i] - a[i+1]:
            k -= a[i] - a[i+1]
            ans += (a[i] - a[i+1]) * (i+1)
            a[i] -= (a[i] - a[i+1])
    ans += (k % n) * (a[0] - k // n)
    print(ans)
