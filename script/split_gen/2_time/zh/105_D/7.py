def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    d = {}
    for x in s:
        if x%m in d:
            d[x%m] += 1
        else:
            d[x%m] = 1
    ans = 0
    for x in d:
        ans += d[x]*(d[x]-1)//2
    print(ans)
