def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    #print(n,k,d,a)
    a.sort(reverse=True)
    #print(a)
    ans = -1
    for i in range(2**n):
        s = 0
        for j in range(n):
            if (i >> j) & 1:
                s += a[j]
        #print(i,s)
        if s % d == 0:
            ans = max(ans,s)
    print(ans)

if __name__ == '__main__':
    main()