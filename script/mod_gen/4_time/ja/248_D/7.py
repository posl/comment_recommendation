def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    from collections import defaultdict
    N = int(readline())
    A = list(map(int,readline().split()))
    Q = int(readline())
    Query = [list(map(int,readline().split())) for i in range(Q)]
    ans = [0]*Q
    for i in range(Q):
        L,R,X = Query[i]
        ans[i] = A[L-1:R].count(X)
    print(*ans,sep='\n')

if __name__ == '__main__':
    main()