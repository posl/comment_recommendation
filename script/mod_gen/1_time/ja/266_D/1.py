def main():
    N = int(input())
    T = []
    X = []
    A = []
    for i in range(N):
        t, x, a = map(int, input().split())
        T.append(t)
        X.append(x)
        A.append(a)
    # すぬけ君が出現する時刻の降順にソート
    T, X, A = zip(*sorted(zip(T, X, A), reverse=True))
    # 捕まえたすぬけ君の大きさの合計
    ans = 0
    # 捕まえたすぬけ君の大きさの合計を更新するかどうか
    update = [False] * N
    # 捕まえたすぬけ君の大きさの合計を更新するかどうかを更新する
    for i in range(N):
        for j in range(i + 1, N):
            # 捕まえたすぬけ君の大きさの合計を更新するかどうかを更新する
            if T[i] - T[j] >= abs(X[i] - X[j]) and not update[j]:
                update[j] = True
    # 捕まえたすぬけ君の大きさの合計を更新する
    for i in range(N):
        if update[i]:
            ans += A[i]
    print(ans)

if __name__ == '__main__':
    main()