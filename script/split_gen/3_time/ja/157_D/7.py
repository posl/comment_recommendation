def main():
    N, M, K = map(int, input().split())
    #友達関係のリスト
    friends = [[] for _ in range(N)]
    #ブロック関係のリスト
    blocks = [[] for _ in range(N)]
    #友達候補のリスト
    candidates = [0] * N
    #友達関係の入力
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a-1].append(b-1)
        friends[b-1].append(a-1)
    #ブロック関係の入力
    for _ in range(K):
        c, d = map(int, input().split())
        blocks[c-1].append(d-1)
        blocks[d-1].append(c-1)
    #友達候補の数をカウント
    for i in range(N):
        candidates[i] = N - len(friends[i]) - 1 #友達関係の数を引く
        for j in friends[i]:
            if i in blocks[j]: #ブロック関係にあるかどうか
                candidates[i] -= 1
    #友達候補の数を出力
    print(' '.join(map(str, candidates)))
