def main():
    A,B,Q = map(int,input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]
    S.sort()
    T.sort()
    import bisect
    for x in X:
        i = bisect.bisect_left(S,x)
        j = bisect.bisect_left(T,x)
        ans = 10**18
        for s in [S[i-1],S[i]]:
            for t in [T[j-1],T[j]]:
                d1,d2 = abs(s-x)+abs(t-s),abs(t-x)+abs(s-t)
                ans = min(ans,d1,d2)
        print(ans)

if __name__ == '__main__':
    main()