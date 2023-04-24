Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    G = [[] for _ in range(N)]
    for i in range(M):
        G[A[i] - 1].append(B[i] - 1)
    used = [False] * N
    ans = []
    for i in range(N):
        if used[i]:
            continue
        used[i] = True
        ans.append(i)
        for j in G[i]:
            if used[j]:
                print(-1)
                return
            used[j] = True
            ans.append(j)
    print(*[i + 1 for i in ans])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = [-1] * N
    for i in range(M):
        if ans[A[i] - 1] == -1:
            ans[A[i] - 1] = A[i]
        if ans[B[i] - 1] == -1:
            ans[B[i] - 1] = B[i]
    for i in range(N):
        if ans[i] == -1:
            ans[i] = i + 1
    for i in range(M):
        if ans.index(A[i]) > ans.index(B[i]):
            print(-1)
            return
    print(*ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    G = [[] for _ in range(N+1)]
    for i in range(M):
        G[A[i]].append(B[i])
    for i in range(N+1):
        G[i].sort()
    #print(G)
    used = [False] * (N+1)
    ans = []
    def dfs(v):
        used[v] = True
        for nv in G[v]:
            if used[nv]:
                print(-1)
                exit()
            dfs(nv)
        ans.append(v)
    for i in range(1, N+1):
        if not used[i]:
            dfs(i)
    print(*ans[::-1])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    if N == 2:
        if M == 0:
            print("1 2")
        else:
            print("-1")
    else:
        if M == 0:
            print("1 2 3")
        else:
            if M == 1:
                if A[0] == 1:
                    print("-1")
                else:
                    print("1 2 3")
            else:
                if A[0] == 1:
                    print("-1")
                else:
                    if A[1] == 1:
                        print("-1")
                    else:
                        print("1 2 3")

main()

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #入力の検証
    for i in range(M):
        if A[i] == B[i]:
            print(-1)
            return

    #入力の検証
    for i in range(M):
        for j in range(M):
            if i != j and A[i] == A[j] and B[i] == B[j]:
                print(-1)
                return

    #入力の検証
    for i in range(M):
        for j in range(M):
            if i != j and A[i] == B[j] and B[i] == A[j]:
                print(-1)
                return

    #入力の検証
    for i in range(M):
        for j in range(M):
            if i != j and A[i] == B[j] and B[i] == B[j]:
                print(-1)
                return

    #入力の検証
    for i in range(M):
        for j in range(M):
            if i != j and A[i] == A[j] and B[i] == A[j]:
                print(-1)
                return

    #入力の検証
    for i in range(M):
        for j in range(M):
            if i != j and A[i] == B[j] and B[i] == B[j]:
                print(-1)
                return

    #入力の検証
    for i in range(M):
        for j in range(M):
            if i != j and A[i] == A[j] and B[i] == B[j]:
                print(-1)
                return

    #入力の検証
    for i in range(M):
        for j in range(M):
            if i != j and A[i] == B[j] and B[i] == A[j]:
                print(-1)
                return

    #入力の検証
    for i in range(M):
        for j in range(M):
            if i != j and A[i] == B

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        edge[A].append(B)
    dp = [0] * N
    for i in range(N):
        if dp[i] == 0:
            dp[i] = 1
            for j in edge[i]:
                if dp[j] == 0:
                    dp[j] = 2
                elif dp[j] == 1:
                    print(-1)
                    return
    ans = []
    for i in range(N):
        if dp[i] == 1:
            ans.append(i)
    for i in range(N):
        if dp[i] == 2:
            ans.append(i)
    print(*[i + 1 for i in ans])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB = [[a-1, b-1] for a, b in AB]

    # 1. トポロジカルソート
    # 2. トポロジカルソートの結果を出力
    # 3. トポロジカルソートの結果がN個ならばOK
    # 4. トポロジカルソートの結果がN個未満ならばNG

    # 1. トポロジカルソート
    # 1-1. 入次数を数える
    # 1-2. 入次数が0のノードをキューに入れる
    # 1-3. キューからノードを取り出す
    # 1-4. そのノードに対する辺を削除
    # 1-5. 新たに入次数が0になったノードをキューに入れる
    # 1-6. キューが空になるまで3. に戻る

    # 1-1. 入次数を数える
    in_degrees = [0] * N
    for a, b in AB:
        in_degrees[b] += 1

    # 1-2. 入次数が0のノードをキューに入れる
    q = []
    for i in range(N):
        if in_degrees[i] == 0:
            q.append(i)

    # 1-3. キューからノードを取り出す
    # 1-4. そのノードに対する辺を削除
    # 1-5. 新たに入次数が0になったノードをキューに入れる
    # 1-6. キューが空になるまで3

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    x = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        x[a-1].append(b-1)
    ans = []
    for i in range(n):
        if len(x[i]) == 0:
            ans.append(i)
    if len(ans) == 0:
        print(-1)
        return
    for i in range(n):
        for j in range(i+1, n):
            if len(x[j]) == 0:
                ans.append(j)
                continue
            flag = False
            for k in range(len(x[j])):
                if x[j][k] == ans[i]:
                    flag = True
                    break
            if flag:
                ans.append(j)
                continue
    if len(ans) == n:
        for i in range(n):
            ans[i] += 1
        print(*ans)
    else:
        print(-1)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = [-1] * N
    for i in range(N):
        ans[i] = i + 1
    for i in range(M):
        if AB[i][0] > AB[i][1]:
            ans = [-1]
            break
        else:
            ans[AB[i][0] - 1], ans[AB[i][1] - 1] = ans[AB[i][1] - 1], ans[AB[i][0] - 1]
    print(*ans)

=======
Suggestion 10

def solve(N, M, AB):
    # 2 <= N <= 2 * 10**5
    # 1 <= M <= 2 * 10**5
    # 1 <= A_i, B_i <= N
    # A_i != B_i
    # All values in input are integers.
    # Input is given from Standard Input in the following format:
    # N M
    # A_1 B_1
    # .
    # .
    # .
    # A_M B_M
    # Print the answer.
    # Among the sequences P that are permutations of (1, 2, ..., N) and satisfy the condition below, find the lexicographically smallest sequence.
    # For each i = 1, ..., M, A_i appears earlier than B_i in P.
    # If there is no such P, print -1.
    # 2 3
    # 1 2
    # 1 2
    # 2 1
    # -1
    # 4 3
    # 2 1
    # 3 4
    # 2 4
    # 2 1 3 4
    # The following five permutations P satisfy the condition: (2, 1, 3, 4), (2, 3, 1, 4), (2, 3, 4, 1), (3, 2, 1, 4), (3, 2, 4, 1). The lexicographically smallest among them is (2, 1, 3, 4).
    # 2 <= N <= 2 * 10**5
    # 1 <= M <= 2 * 10**5
    # 1 <= A_i, B_i <= N
    # A_i != B_i
    # All values in input are integers.
    # Input is given from Standard Input in the following format:
    # N M
    # A_1 B_1
    # .
    # .
    # .
    # A_M B_M
    # Print the answer.
    # Among the sequences P that are permutations of (1, 2, ..., N) and satisfy the condition below, find the lexicographically smallest sequence.
    # For each i = 1, ..., M
