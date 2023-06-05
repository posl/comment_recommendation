def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    ans = -1
    for i in range(n):
        for j in range(i+1,n):
            if (a[i]+a[j]) % d == 0:
                ans = max(ans,a[i]+a[j])
    print(ans)
