def problem267_c():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    ans = -float("inf")
    for i in range(m,n+1):
        ans = max(ans,s[i]-s[i-m])
    print(ans)
problem267_c()

if __name__ == '__main__':
    problem267_c()