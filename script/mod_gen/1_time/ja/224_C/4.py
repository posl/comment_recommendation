def main():
    N = int(input())
    P = [tuple(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                # 点の位置関係を調べる
                # 3点が一直線上にある場合は、面積が0になるのでスキップ
                if (P[j][0] - P[i][0]) * (P[k][1] - P[i][1]) == (P[j][1] - P[i][1]) * (P[k][0] - P[i][0]):
                    continue
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()