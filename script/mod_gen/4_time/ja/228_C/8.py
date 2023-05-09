def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    # 3日間の合計点を計算
    S = [sum(p) for p in P]
    # 4日目の点数を計算
    Q = [S[i] + 300 for i in range(N)]
    # 4日目の点数でソート
    Q.sort(reverse=True)
    # K位以内に入っているかどうか判定
    for i in range(N):
        if Q.index(S[i] + 300) < K:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()