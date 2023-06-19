def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0 for i in range(n)]
    b[0] = a[0]%m
    for i in range(1,n):
        b[i] = (a[i]+b[i-1])%m
    c = [0 for i in range(m)]
    for i in range(n):
        c[b[i]] += 1
    ans = 0
    for i in range(m):
        ans += c[i]*(c[i]-1)//2
    ans += c[0]
    print(ans)
