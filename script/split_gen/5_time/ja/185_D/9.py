def main():
    n,m = map(int,input().split())
    if m == 0:
        print(1)
        return
    a = list(map(int,input().split()))
    a.sort()
    if a[0] != 1:
        a.insert(0,0)
    if a[-1] != n:
        a.append(n+1)
    
    if len(a) == 2:
        print(1)
        return
    
    if len(a) == 3:
        print(2)
        return
    
    k = []
    for i in range(1,len(a)):
        k.append(a[i]-a[i-1]-1)
    
    k = list(filter(lambda a: a != 0, k))
    k.sort()
    min_k = k[0]
    ans = 0
    for i in range(len(k)):
        ans += k[i]//min_k
        if k[i]%min_k != 0:
            ans += 1
    print(ans)
