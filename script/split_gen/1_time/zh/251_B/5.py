def main():
    n,w = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    #print(a)
    #print(n,w)
    #print(a[0],a[1],a[2])
    #print(a[0]+a[1]+a[2])
    #print(a[0]+a[1])
    #print(a[0]+a[2])
    #print(a[1]+a[2])
    #print(a[0])
    #print(a[1])
    #print(a[2])
    ans = 0
    for i in range(n):
        for j in range(i,n):
            for k in range(j,n):
                if a[i]+a[j]+a[k] <= w:
                    ans += 1
    print(ans)
