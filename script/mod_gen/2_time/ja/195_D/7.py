def solve():
    N, M, Q = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    LR = [list(map(int, input().split())) for _ in range(Q)]
    for l, r in LR:
        x = X[:l - 1] + X[r:]
        x.sort()
        wv.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for w, v in wv:
            for i in range(len(x)):
                if x[i] >= w:
                    ans += v
                    x[i] = 0
                    break
        print(ans)
solve()

if __name__ == '__main__':
    solve()