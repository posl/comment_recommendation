def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0]
    for i in range(n):
        b.append(b[i]+a[i])
    print(b)
    ans = -float("inf")
    for i in range(m,n+1):
        ans = max(ans,b[i]-b[i-m])
    print(ans)
