def solve():
    N,M,Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    W = [w for w,v in WV]
    V = [v for w,v in WV]
    X = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(Q)]
    for query in queries:
        L,R = query
        boxes = X[:L-1] + X[R:]
        boxes.sort()
        ans = 0
        for box in boxes:
            for i in range(N):
                if W[i] <= box:
                    ans += V[i]
                    W[i] = 10**9
                    break
        print(ans)

if __name__ == '__main__':
    solve()