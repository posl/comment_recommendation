def solve():
    N, M, Q = map(int, input().split())
    WV = [tuple(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(Q)]
    WV.sort(key=lambda wv: wv[1], reverse=True)
    X.sort(reverse=True)
    for L, R in queries:
        boxes = X[:L-1] + X[R:]
        boxes.sort(reverse=True)
        ans = 0
        for w, v in WV:
            for i, box in enumerate(boxes):
                if w <= box:
                    ans += v
                    del boxes[i]
                    break
        print(ans)

if __name__ == '__main__':
    solve()