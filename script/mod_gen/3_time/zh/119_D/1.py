def main():
    #A,B,Q = map(int,input().split())
    A,B,Q = 2,3,4
    #s = [int(input()) for i in range(A)]
    s = [100,600]
    #t = [int(input()) for i in range(B)]
    t = [400,900,1000]
    #x = [int(input()) for i in range(Q)]
    x = [150,2000,899,799]
    for i in range(Q):
        l = 0
        r = 0
        while l < A and s[l] < x[i]:
            l += 1
        while r < B and t[r] < x[i]:
            r += 1
        ans = 10 ** 20
        for j in range(l-1,l+1):
            for k in range(r-1,r+1):
                d1 = abs(s[j]-x[i]) + abs(t[k]-s[j])
                d2 = abs(t[k]-x[i]) + abs(s[j]-t[k])
                ans = min(ans,d1,d2)
        print(ans)

if __name__ == '__main__':
    main()