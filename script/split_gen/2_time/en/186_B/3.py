def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 100 * 100
    for h in range(H):
        for w in range(W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    cnt += abs(i - h) + abs(j - w)
            ans = min(ans, cnt * A[h][w])
    print(ans)
