def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    ans = -1
    for i in range(n-k+1):
        if (a[i]-a[i+k-1])%d == 0:
            ans = max(ans,a[i+k-1])
    print(ans)
