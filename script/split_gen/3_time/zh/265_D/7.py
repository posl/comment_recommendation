def main():
    n,p,q,r = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    #print(a)
    s = [0]
    for i in range(n):
        s.append(s[i]+a[i])
    #print(s)
    ans = 0
    for i in range(n-1):
        if a[i] > q:
            break
        for j in range(i+1,n):
            if a[j] > r:
                break
            ans = max(ans,p*a[i]+q*(a[j]-a[i])+r*(s[n]-s[j]))
    print(ans)
