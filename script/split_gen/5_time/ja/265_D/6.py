def main():
    n,p,q,r = map(int,input().split())
    a = list(map(int,input().split()))
    ans = "No"
    for i in range(n-3):
        for j in range(i+1,n-2):
            for k in range(j+1,n-1):
                for l in range(k+1,n):
                    if (a[i]+a[i+1]+a[j]+a[j+1]+a[k]+a[k+1]) == p and (a[j]+a[j+1]+a[k]+a[k+1]+a[l]+a[l+1]) == q and (a[k]+a[k+1]+a[l]+a[l+1]+a[i]+a[i+1]) == r:
                        ans = "Yes"
                        break
    print(ans)
