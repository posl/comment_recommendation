def main():
    N, M, K = map(int, input().split())
    # フレンド関係のリスト
    friend = [[] for _ in range(N)]
    # ブロック関係のリスト
    block = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friend[a - 1].append(b - 1)
        friend[b - 1].append(a - 1)
    for _ in range(K):
        c, d = map(int, input().split())
        block[c - 1].append(d - 1)
        block[d - 1].append(c - 1)
    # 各ユーザーのフレンド候補数
    ans = [0] * N
    # 各ユーザーのフレンド候補数を求める
    for i in range(N):
        # 自分自身のユーザー番号を除く
        ans[i] = N - 1 - len(friend[i]) - len(block[i])
        # ブロックしているユーザーのフレンド候補数を1減らす
        for b in block[i]:
            if b in friend[i]:
                ans[i] -= 1
        # 自分自身のユーザー番号を除く
        ans[i] -= 1
    # フレンド関係のユーザーのフレンド候補数を1減らす
    for i in range(N):
        for f in friend[i]:
            if f < i:
                continue
            ans[f] -= 1
    # フレンド候補数を出力
    print(' '.join(map(str, ans)))
