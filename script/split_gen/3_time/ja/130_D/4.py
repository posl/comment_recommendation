def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[-1] + a[i])
    ans = 0
    r = 0
    for l in range(n+1):
        while r < n+1 and s[r] - s[l] < k:
            r += 1
        ans += n - r + 1
    print(ans)
