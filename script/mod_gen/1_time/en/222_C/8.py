def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2 * N)]
    # 残りの試合をする順番
    order = [i for i in range(2 * N)]
    for i in range(M):
        # 残りの試合をする順番を試合ごとに更新
        new_order = []
        for j in range(0, 2 * N, 2):
            # 試合の勝者を決める
            winner = order[j] if judge(A[order[j]][i], A[order[j + 1]][i]) else order[j + 1]
            new_order.append(winner)
        order = new_order
    # 結果を出力
    for i in order:
        print(i + 1)

if __name__ == '__main__':
    main()