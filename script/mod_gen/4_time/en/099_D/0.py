def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # 各色の数をカウント
    cnt = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cnt[(i + j) % 3][c[i][j] - 1] += 1
    # 各色の組み合わせについて、各色をどの色に塗り替えるかを全探索
    ans = 10 ** 18
    for c1 in range(C):
        for c2 in range(C):
            if c1 == c2:
                continue
            for c3 in range(C):
                if c1 == c3 or c2 == c3:
                    continue
                tmp = 0
                for i in range(C):
                    tmp += cnt[0][i] * D[i][c1]
                    tmp += cnt[1][i] * D[i][c2]
                    tmp += cnt[2][i] * D[i][c3]
                ans = min(ans, tmp)
    print(ans)
main()

if __name__ == '__main__':
    main()