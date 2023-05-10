def main():
    A,B,Q = map(int,input().split())
    s = [0]*A
    t = [0]*B
    x = [0]*Q
    for i in range(A):
        s[i] = int(input())
    for i in range(B):
        t[i] = int(input())
    for i in range(Q):
        x[i] = int(input())
    s = [-float('inf')]+s+[float('inf')]
    t = [-float('inf')]+t+[float('inf')]
    for i in range(Q):
        l = bisect.bisect_left(s,x[i])
        r = bisect.bisect_left(t,x[i])
        ans = float('inf')
        for j in [s[l-1],s[l]]:
            for k in [t[r-1],t[r]]:
                d1 = abs(j-x[i])+abs(k-j)
                d2 = abs(k-x[i])+abs(j-k)
                ans = min(ans,d1,d2)
        print(ans)

if __name__ == '__main__':
    main()