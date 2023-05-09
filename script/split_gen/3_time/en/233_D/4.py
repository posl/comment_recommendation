def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[-1]+a[i])
    d = {}
    for i in range(n+1):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    ans = 0
    for i in range(n+1):
        if s[i]+k in d:
            ans += d[s[i]+k]
    print(ans)
