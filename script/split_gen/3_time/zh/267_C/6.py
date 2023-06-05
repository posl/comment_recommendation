def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.insert(0,0)
    for i in range(n):
        a[i+1] += a[i]
    ans = -10**10
    for i in range(n-m+1):
        ans = max(ans,a[i+m]-a[i])
    for i in range(1,m+1):
        ans += i*a[i]
    print(ans)
