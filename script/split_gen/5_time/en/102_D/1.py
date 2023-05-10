def main():
    n = int(input())
    a = list(map(int, input().split()))
    cum = [0] * (n+1)
    for i in range(n):
        cum[i+1] = cum[i] + a[i]
    ans = 10**9
    for i in range(1, n-2):
        for j in range(i+1, n-1):
            p = cum[i+1]
            q = cum[j+1] - cum[i+1]
            r = cum[n] - cum[j+1]
            s = cum[n] - cum[j+1]
            ans = min(ans, max(p, q, r, s) - min(p, q, r, s))
    print(ans)
