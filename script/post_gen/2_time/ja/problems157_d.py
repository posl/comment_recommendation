Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    #友達リスト
    friends = [[] for _ in range(N)]
    for a, b in AB:
        friends[a-1].append(b-1)
        friends[b-1].append(a-1)
    #ブロックリスト
    blocks = [[] for _ in range(N)]
    for c, d in CD:
        blocks[c-1].append(d-1)
        blocks[d-1].append(c-1)
    #友達候補
    ans = [0] * N
    for i in range(N):
        cnt = 0
        for j in friends[i]:
            if j in friends[i] and j not in blocks[i]:
                cnt += 1
        ans[i] = len(friends[i]) - cnt
        ans[i] -= 1
    print(*ans)

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    F = [set() for _ in range(N)]
    B = [set() for _ in range(N)]
    for a, b in AB:
        F[a - 1].add(b - 1)
        F[b - 1].add(a - 1)
    for c, d in CD:
        B[c - 1].add(d - 1)
        B[d - 1].add(c - 1)
    ans = [0] * N
    for i in range(N):
        ans[i] = N - len(F[i]) - 1
        for j in F[i]:
            if i in F[j]:
                ans[i] -= 1
        for j in B[i]:
            if j in F[i]:
                ans[i] -= 1
    print(*ans)

=======
Suggestion 3

def main():
    N, M, K = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * K
    D = [0] * K
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(K):
        C[i], D[i] = map(int, input().split())
    #友達関係をリスト化
    friend = [[] for _ in range(N+1)]
    for i in range(M):
        friend[A[i]].append(B[i])
        friend[B[i]].append(A[i])
    #ブロック関係をリスト化
    block = [[] for _ in range(N+1)]
    for i in range(K):
        block[C[i]].append(D[i])
        block[D[i]].append(C[i])
    #人iの友達候補数を求める
    ans = [0] * (N+1)
    for i in range(1, N+1):
        ans[i] = N - len(friend[i]) - 1
        for j in friend[i]:
            if i in block[j]:
                ans[i] -= 1
    for i in range(1, N+1):
        print(ans[i], end=" ")

=======
Suggestion 4

def main():
    N, M, K = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(K):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    #友達関係
    rel = [[0] * N for i in range(N)]
    for i in range(M):
        rel[A[i] - 1][B[i] - 1] = 1
        rel[B[i] - 1][A[i] - 1] = 1
    #ブロック関係
    bl = [[0] * N for i in range(N)]
    for i in range(K):
        bl[C[i] - 1][D[i] - 1] = 1
        bl[D[i] - 1][C[i] - 1] = 1
    #友達候補
    ans = [0] * N
    for i in range(N):
        for j in range(N):
            if rel[i][j] == 1 and bl[i][j] == 0:
                ans[i] += 1
    for i in range(N):
        ans[i] -= 1
    #友達候補の数
    for i in range(N):
        for j in range(N):
            if rel[i][j] == 1:
                ans[i] -= 1
                ans[j] -= 1
    for i in range(N):
        print(ans[i], end = " ")
    print()

=======
Suggestion 5

def main():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N)]
    blocks = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a-1].append(b-1)
        friends[b-1].append(a-1)
    for _ in range(K):
        c, d = map(int, input().split())
        blocks[c-1].append(d-1)
        blocks[d-1].append(c-1)
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
Suggestion 6

def main():
    n, m, k = map(int, input().split())
    friends = [set() for _ in range(n)]
    block = [set() for _ in range(n)]
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
        block[c].add(d)
        block[d].add(c)
    ans = [0]*n
    for i in range(n):
        ans[i] = len(friends[i]) + len(block[i])
    for i in range(n):
        for j in friends[i]:
            if i in friends[j]:
                ans[i] -= 1
                ans[j] -= 1
    for i in range(n):
        ans[i] -= len(friends[i])
        ans[i] -= len(block[i])
        ans[i] += 1
    print(*ans)

=======
Suggestion 7

def main():
    N, M, K = map(int, input().split())
    friend_list = [[] for _ in range(N)]
    block_list = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        friend_list[A-1].append(B-1)
        friend_list[B-1].append(A-1)
    for _ in range(K):
        C, D = map(int, input().split())
        block_list[C-1].append(D-1)
        block_list[D-1].append(C-1)

    ans = [0] * N
    for i in range(N):
        ans[i] = N - len(friend_list[i]) - 1
        for j in friend_list[i]:
            if i in block_list[j]:
                ans[i] -= 1
    print(*ans)

=======
Suggestion 8

def main():
    N, M, K = map(int, input().split())
    F = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        F[a-1][b-1] = F[b-1][a-1] = 1
    B = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        c, d = map(int, input().split())
        B[c-1][d-1] = B[d-1][c-1] = 1
    ans = [0]*N
    for i in range(N):
        for j in range(i+1, N):
            if F[i][j] == 1:
                ans[i] += 1
                ans[j] += 1
    for i in range(N):
        for j in range(N):
            if B[i][j] == 1:
                ans[i] -= 1
                ans[j] -= 1
    for i in range(N):
        ans[i] = N - ans[i] - 1
    print(*ans)

=======
Suggestion 9

def main():
    N, M, K = map(int, input().split())
    #友達関係
    friend = [[] for _ in range(N + 1)]
    #ブロック関係
    block = [[] for _ in range(N + 1)]
    #友達候補
    candidate = [0] * (N + 1)
    #友達関係の数
    friend_num = [0] * (N + 1)
    #友達関係の数の最大値
    max_friend_num = 0
    #友達関係の数の最大値の人の数
    max_friend_num_people = 0
    #友達関係の数の最大値の人のリスト
    max_friend_num_people_list = []
    #友達候補の数
    candidate_num = [0] * (N + 1)
    #友達候補の数の最大値
    max_candidate_num = 0
    #友達候補の数の最大値の人の数
    max_candidate_num_people = 0
    #友達候補の数の最大値の人のリスト
    max_candidate_num_people_list = []

    #友達関係とブロック関係を入力
    for i in range(M):
        A, B = map(int, input().split())
        friend[A].append(B)
        friend[B].append(A)
        friend_num[A] += 1
        friend_num[B] += 1
    for i in range(K):
        C, D = map(int, input().split())
        block[C].append(D)
        block[D].append(C)

    #友達関係の数の最大値と最大値の人の数とリストを求める
    for i in range(1, N + 1):
        if max_friend_num < friend_num[i]:
            max_friend_num = friend_num[i]
            max_friend_num_people = 1
            max_friend_num_people_list = [i]
        elif max_friend_num == friend_num[i]:
            max_friend

=======
Suggestion 10

def solve(N, M, K, friend, block):
    #友達関係のグラフを作成
    friend_graph = [[] for i in range(N)]
    for a, b in friend:
        friend_graph[a - 1].append(b - 1)
        friend_graph[b - 1].append(a - 1)
    #ブロック関係のグラフを作成
    block_graph = [[] for i in range(N)]
    for c, d in block:
        block_graph[c - 1].append(d - 1)
        block_graph[d - 1].append(c - 1)
    #友達候補の数を求める
    ans = [0] * N
    for i in range(N):
        #自分自身と友達関係にない人を数える
        ans[i] = N - len(friend_graph[i]) - 1
        #ブロック関係になっている人を引く
        for j in block_graph[i]:
            if j in friend_graph[i]:
                ans[i] -= 1
    return ans
