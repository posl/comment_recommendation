def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = float('inf')
    # 1回目の駅の選び方
    for i in range(H):
        for j in range(W):
            # 2回目の駅の選び方
            for k in range(i, H):
                for l in range(W):
                    # 同じマスを選んだ場合はスキップ
                    if i == k and j == l:
                        continue
                    # 1回目の駅の建設費用
                    cost1 = A[i][j]
                    # 2回目の駅の建設費用
                    cost2 = A[k][l]
                    # 線路の建設費用
                    cost3 = C * (abs(i - k) + abs(j - l))
                    ans = min(ans, cost1 + cost2 + cost3)
    print(ans)

if __name__ == '__main__':
    main()