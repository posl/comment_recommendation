def main():
    #n,k,x = map(int,input().split())
    n,k,x = 5,4,7
    #a = list(map(int,input().split()))
    a = [8,3,10,5,13]
    a.sort()
    #print(a)
    ans = 0
    for i in range(n):
        if k > 0:
            ans += max(a[i]-x,0)
            #print(ans)
            k -= 1
        else:
            ans += a[i]
            #print(ans)
    print(ans)

if __name__ == '__main__':
    main()