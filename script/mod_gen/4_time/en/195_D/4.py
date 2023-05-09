def solve():
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    LR = [list(map(int, input().split())) for _ in range(Q)]
    WV.sort(key=lambda x: x[1], reverse=True)
    for l, r in LR:
        boxes = X[:l-1] + X[r:]
        boxes.sort()
        used = [False] * (N+1)
        ans = 0
        for box in boxes:
            for i in range(N):
                if not used[i] and WV[i][0] <= box:
                    used[i] = True
                    ans += WV[i][1]
                    break
        print(ans)

if __name__ == '__main__':
    solve()