def solve():
    import sys
    input = sys.stdin.readline
    A,B,Q = map(int,input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    s = [-float("inf")]+s+[float("inf")]
    t = [-float("inf")]+t+[float("inf")]
    from bisect import bisect_left,bisect_right
    def f(x):
        i = bisect_left(s,x)
        j = bisect_left(t,x)
        return min(
            max(s[i],t[j])-x,
            x-min(s[i-1],t[j-1]),
            s[i]-t[j-1]+min(s[i]-x,x-t[j-1]),
            t[j]-s[i-1]+min(t[j]-x,x-s[i-1])
        )
    print(*map(f,x),sep="\n")
solve()

if __name__ == '__main__':
    solve()