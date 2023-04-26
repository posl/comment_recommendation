Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]

    #友達関係
    friend = [[0 for _ in range(N)] for _ in range(N)]
    for a, b in AB:
        friend[a-1][b-1] = 1
        friend[b-1][a-1] = 1

    #ブロック関係
    block = [[0 for _ in range(N)] for _ in range(N)]
    for c, d in CD:
        block[c-1][d-1] = 1
        block[d-1][c-1] = 1

    #友達候補
    ans = [0 for _ in range(N)]
    for i in range(N):
        #自分自身と友達関係にある人数
        ans[i] = sum(friend[i]) - 1
        #ブロック関係にある人数
        for j in range(N):
            if block[i][j] == 1 and friend[i][j] == 1:
                ans[i] -= 1

    print(*ans)

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    #友達関係
    friend = [[0] * (N+1) for _ in range(N+1)]
    for a, b in AB:
        friend[a][b] = 1
        friend[b][a] = 1
    #ブロック関係
    block = [[0] * (N+1) for _ in range(N+1)]
    for c, d in CD:
        block[c][d] = 1
        block[d][c] = 1
    #友達候補
    ans = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(1, N+1):
            if friend[i][j] == 1 and block[i][j] == 0:
                ans[i] += 1
    for i in range(1, N+1):
        ans[i] -= 1
    for i in range(1, N+1):
        for j in range(1, N+1):
            if friend[i][j] == 1:
                ans[i] -= 1
                ans[j] -= 1
    for i in range(1, N+1):
        print(ans[i], end=" ")

=======
Suggestion 3

def main():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N)]
    blocks = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a - 1].append(b - 1)
        friends[b - 1].append(a - 1)
    for _ in range(K):
        c, d = map(int, input().split())
        blocks[c - 1].append(d - 1)
        blocks[d - 1].append(c - 1)
    ans = [0] * N
    for i in range(N):
        ans[i] = N - 1 - len(friends[i]) - len(blocks[i])
        for j in range(N):
            if j in friends[i]:
                ans[i] -= 1
            elif j in blocks[i]:
                ans[i] -= 1
    print(*ans)

=======
Suggestion 4

def main():
    N, M, K = map(int, input().split())
    F = [[] for _ in range(N)]
    B = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        F[a-1].append(b-1)
        F[b-1].append(a-1)
    for _ in range(K):
        c, d = map(int, input().split())
        B[c-1].append(d-1)
        B[d-1].append(c-1)
    ans = [0] * N
    for i in range(N):
        ans[i] = N - len(F[i]) - 1 - len(B[i])
        for j in F[i]:
            if i in B[j]:
                ans[i] -= 1
    print(*ans)

=======
Suggestion 5

def main():
    N, M, K = map(int, input().split())
    friend = [list(map(int, input().split())) for _ in range(M)]
    block = [list(map(int, input().split())) for _ in range(K)]

    #友達関係をリスト化
    friend_list = [[] for _ in range(N+1)]
    for f in friend:
        friend_list[f[0]].append(f[1])
        friend_list[f[1]].append(f[0])

    #ブロック関係をリスト化
    block_list = [[] for _ in range(N+1)]
    for b in block:
        block_list[b[0]].append(b[1])
        block_list[b[1]].append(b[0])

    #友達候補の数を計算
    for i in range(1, N+1):
        #友達候補の数 = 友達関係の数 - ブロック関係の数 - 自分自身
        ans = len(friend_list[i]) - len(block_list[i]) - 1
        print(ans, end=" ")

=======
Suggestion 6

def main():
    N, M, K = map(int, input().split())
    friends = [set() for _ in range(N)]
    block = [set() for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        friends[A].add(B)
        friends[B].add(A)
    for _ in range(K):
        C, D = map(int, input().split())
        C -= 1
        D -= 1
        block[C].add(D)
        block[D].add(C)
    for i in range(N):
        friends[i].add(i)
        block[i].add(i)
    for i in range(N):
        for f in friends[i]:
            block[i] |= block[f]
    for i in range(N):
        print(len(friends[i] & block[i]) - 1, end=' ')
    print()

=======
Suggestion 7

def main():
    N, M, K = map(int, input().split())
    relation = [[0] * N for _ in range(N)]
    block = [[0] * N for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        relation[A - 1][B - 1] = 1
        relation[B - 1][A - 1] = 1
    for _ in range(K):
        C, D = map(int, input().split())
        block[C - 1][D - 1] = 1
        block[D - 1][C - 1] = 1
    ans = [0] * N
    for i in range(N):
        for j in range(N):
            if relation[i][j] == 1:
                ans[i] += 1
                ans[j] += 1
    for i in range(N):
        for j in range(N):
            if block[i][j] == 1:
                ans[i] -= 1
                ans[j] -= 1
    for i in range(N):
        ans[i] -= 1
    print(*ans)

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    N, M, K = map(int, input().split())
    #友達関係のリスト
    friends = [[] for _ in range(N)]
    #ブロック関係のリスト
    blocks = [[] for _ in range(N)]

    #友達関係のリストを作る
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a-1].append(b-1)
        friends[b-1].append(a-1)
    
    #ブロック関係のリストを作る
    for _ in range(K):
        c, d = map(int, input().split())
        blocks[c-1].append(d-1)
        blocks[d-1].append(c-1)

    #友達候補の数を数える
    for i in range(N):
        #友達候補の数
        ans = 0
        #友達候補の数を数える
        for j in friends[i]:
            #友達関係にある人の友達候補を数える
            ans += len(friends[j])
            #ブロック関係にある人の友達候補を引く
            for k in blocks[j]:
                if k in friends[i]:
                    ans -= 1
        #友達関係にある人の友達候補を引く
        for j in friends[i]:
            ans -= len(friends[j])
        #ブロック関係にある人の友達候補を引く
        for j in blocks[i]:
            ans -= len(friends[j])
        #友達候補の数を出力
        print(ans, end=' ')
    print()

=======
Suggestion 10

def main():
    N, M, K = map(int, input().split())
    #友達関係
    friend = {}
    for i in range(M):
        a, b = map(int, input().split())
        if a in friend:
            friend[a].append(b)
        else:
            friend[a] = [b]

        if b in friend:
            friend[b].append(a)
        else:
            friend[b] = [a]

    #ブロック関係
    block = {}
    for i in range(K):
        c, d = map(int, input().split())
        if c in block:
            block[c].append(d)
        else:
            block[c] = [d]

        if d in block:
            block[d].append(c)
        else:
            block[d] = [c]

    #友達候補
    ans = [0] * N
    for i in range(N):
        ans[i] = N - 1

        if i + 1 in friend:
            ans[i] -= len(friend[i + 1])

        if i + 1 in block:
            for j in block[i + 1]:
                if j in friend:
                    if i + 1 in friend[j]:
                        ans[i] -= 1

    print(*ans)
