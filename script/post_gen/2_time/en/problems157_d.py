Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    # print(N, M, K)
    # print(AB)
    # print(CD)

    # 関係を持つ人を記録
    # 1: 友達
    # 2: ブロック
    # 0: その他
    relation = [[0 for _ in range(N)] for _ in range(N)]
    for a, b in AB:
        relation[a-1][b-1] = 1
        relation[b-1][a-1] = 1
    for c, d in CD:
        relation[c-1][d-1] = 2
        relation[d-1][c-1] = 2

    # print(relation)

    # 人ごとに友達候補数をカウント
    ans = [0 for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if relation[i][j] == 1:
                ans[i] += 1
                ans[j] += 1

    # print(ans)

    # ブロック関係の人を引く
    for c, d in CD:
        if relation[c-1][d-1] == 2:
            ans[c-1] -= 1
            ans[d-1] -= 1

    # print(ans)

    # 自分自身と友達関係の人を引く
    for i in range(N):
        ans[i] -= relation[i][i]

    # print(ans)

    # 結果を出力
    for a in ans:
        print(a, end=" ")

main()

=======
Suggestion 2

def solve():
    N, M, K = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * K
    D = [0] * K
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(K):
        C[i], D[i] = map(int, input().split())
    ans = [0] * N
    for i in range(M):
        ans[A[i]-1] += 1
        ans[B[i]-1] += 1
    for i in range(K):
        if A[C[i]-1] == D[i]:
            ans[C[i]-1] -= 1
        if B[D[i]-1] == C[i]:
            ans[D[i]-1] -= 1
    for i in range(N):
        ans[i] = N - ans[i] - 1
    print(" ".join(map(str, ans)))

=======
Suggestion 3

def main():
    n, m, k = map(int, input().split())
    friends = [set() for _ in range(n)]
    blocks = [set() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        friends[a].add(b)
        friends[b].add(a)
    for _ in range(k):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        blocks[c].add(d)
        blocks[d].add(c)
    ans = [0] * n
    for i in range(n):
        ans[i] = n - len(friends[i]) - 1 - len(blocks[i])
        for j in friends[i]:
            if i in friends[j]:
                ans[i] -= 1
    print(' '.join(map(str, ans)))

=======
Suggestion 4

def main():
    #input
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]

    #solve
    ans = [0]*N
    for i in range(M):
        ans[AB[i][0]-1] += 1
        ans[AB[i][1]-1] += 1

    for i in range(K):
        if AB[i][0] in CD[i]:
            ans[AB[i][0]-1] -= 1
        if AB[i][1] in CD[i]:
            ans[AB[i][1]-1] -= 1

    #output
    for i in range(N):
        print(ans[i])

=======
Suggestion 5

def main():
    N, M, K = map(int, input().split())
    friend = [[] for i in range(N)]
    block = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        friend[A - 1].append(B - 1)
        friend[B - 1].append(A - 1)
    for i in range(K):
        C, D = map(int, input().split())
        block[C - 1].append(D - 1)
        block[D - 1].append(C - 1)
    for i in range(N):
        friend[i].sort()
        block[i].sort()
    for i in range(N):
        cnt = 0
        for j in friend[i]:
            if i not in friend[j]:
                cnt += 1
        for j in block[i]:
            if i in friend[j]:
                cnt -= 1
        print(N - len(friend[i]) - cnt - 1, end = ' ')
    print()

=======
Suggestion 6

def solve():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N)]
    blocks = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        friends[A-1].append(B-1)
        friends[B-1].append(A-1)
    for _ in range(K):
        C, D = map(int, input().split())
        blocks[C-1].append(D-1)
        blocks[D-1].append(C-1)
    ans = [0] * N
    for i in range(N):
        ans[i] = N - len(friends[i]) - 1
        for j in friends[i]:
            if i in friends[j]:
                ans[i] -= 1
        for j in blocks[i]:
            if j in friends[i]:
                ans[i] -= 1
    print(*ans)

=======
Suggestion 7

def main():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N+1)]
    blocks = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)
    for _ in range(K):
        c, d = map(int, input().split())
        blocks[c].append(d)
        blocks[d].append(c)
    for i in range(1, N+1):
        ans = N - len(friends[i]) - 1
        for b in blocks[i]:
            if b in friends[i]:
                ans -= 1
        print(ans, end=" ")

=======
Suggestion 8

def main():
    n, m, k = map(int, input().split())
    friend = [[0] * n for _ in range(n)]
    block = [[0] * n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        friend[a - 1][b - 1] = 1
        friend[b - 1][a - 1] = 1
    for _ in range(k):
        c, d = map(int, input().split())
        block[c - 1][d - 1] = 1
        block[d - 1][c - 1] = 1
    ans = [0] * n
    for i in range(n):
        ans[i] = n - 1 - sum(friend[i]) - sum(block[i])
        for j in range(n):
            if friend[i][j] == 1:
                ans[i] -= 1
    for i in range(n):
        if friend[i][i] == 1:
            ans[i] += 1
    for i in range(n):
        print(ans[i], end = " ")
    print()

=======
Suggestion 9

def main():
  N, M, K = map(int, input().split())
  f = [set() for _ in range(N)]
  b = [set() for _ in range(N)]
  for _ in range(M):
    a, b = map(int, input().split())
    f[a-1].add(b-1)
    f[b-1].add(a-1)
  for _ in range(K):
    c, d = map(int, input().split())
    b[c-1].add(d-1)
    b[d-1].add(c-1)
  ans = [0] * N
  for i in range(N):
    ans[i] = N - 1 - len(f[i]) - len(b[i])
  for i in range(N):
    for j in f[i]:
      if i in f[j]:
        ans[i] -= 1
        ans[j] -= 1
  print(*ans)

=======
Suggestion 10

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
