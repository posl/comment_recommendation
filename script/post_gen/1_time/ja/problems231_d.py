Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A = sorted(A)
    B = sorted(B)
    print("Yes" if A[M - 1] < B[0] else "No")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # 条件を満たす並べ方が存在するか判定してください
    if N == 2 and M == 0:
        print('Yes')
    elif N == 2 and M == 1:
        if A[0] == 1 and B[0] == 2:
            print('Yes')
        else:
            print('No')
    elif N == 3 and M == 0:
        print('Yes')
    elif N == 3 and M == 1:
        if A[0] == 1 and B[0] == 2:
            print('Yes')
        elif A[0] == 2 and B[0] == 3:
            print('Yes')
        elif A[0] == 1 and B[0] == 3:
            print('Yes')
        else:
            print('No')
    elif N == 3 and M == 2:
        if A[0] == 1 and B[0] == 2 and A[1] == 2 and B[1] == 3:
            print('Yes')
        elif A[0] == 1 and B[0] == 3 and A[1] == 2 and B[1] == 3:
            print('Yes')
        elif A[0] == 1 and B[0] == 2 and A[1] == 1 and B[1] == 3:
            print('Yes')
        elif A[0] == 1 and B[0] == 3 and A[1] == 1 and B[1] == 2:
            print('Yes')
        else:
            print('No')
    elif N == 3 and M == 3:
        if A[0] == 1 and B[0] == 2 and A[1] == 2 and B[1] == 3 and A[2] == 1 and B[2] == 3:
            print('Yes')
        else:
            print('No')
    else:

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    A = [0] * m
    B = [0] * m
    for i in range(m):
        A[i], B[i] = map(int, input().split())
    if m == 0:
        print('Yes')
        return
    if n == 2:
        print('No')
        return
    if n == 3:
        if m == 1:
            print('Yes')
        else:
            print('No')
        return
    if m == n - 1:
        print('Yes')
        return
    print('No')

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)
    used = [False] * n
    used[0] = True
    stack = [0]
    while stack:
        v = stack.pop()
        for u in edge[v]:
            if used[u]:
                continue
            used[u] = True
            stack.append(u)
    print("Yes" if all(used) else "No")

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    if m == 0:
        print("Yes")
        return
    for i in range(n):
        if len(g[i]) == 1:
            print("Yes")
            return
    print("No")

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    if M == 0:
        print('Yes')
        return
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    if N == 2 and M > 0:
        print('No')
        return
    if N == 3 and M > 1:
        print('No')
        return

    ans = 'Yes'
    for i in range(M):
        if A[i] == 1 and B[i] == N:
            ans = 'No'
            break
        if A[i] == 1 and B[i] == N-1:
            ans = 'No'
            break
        if A[i] == 2 and B[i] == N:
            ans = 'No'
            break
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    # 隣接リスト
    neighbors = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        neighbors[a-1].append(b-1)
        neighbors[b-1].append(a-1)

    # 連結成分の数を数える
    visited = [False] * N
    count = 0
    for i in range(N):
        if visited[i]:
            continue
        count += 1
        stack = [i]
        while stack:
            j = stack.pop()
            if visited[j]:
                continue
            visited[j] = True
            stack.extend(neighbors[j])

    # 連結成分の数が 1 なら Yes
    print('Yes' if count == 1 else 'No')

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    X = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        if a + 1 == b:
            X[a] += 1
        elif b + 1 == a:
            X[b] += 1
        else:
            print("No")
            exit()
    if sum(X) == M:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    # 入力
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    # 連結要素の個数を数える
    group = [i for i in range(N+1)]
    size = [1] * (N+1)

    def root(x):
        if group[x] == x:
            return x
        else:
            group[x] = root(group[x])
            return group[x]

    def unite(x, y):
        x = root(x)
        y = root(y)
        if x == y:
            return
        if size[x] < size[y]:
            x, y = y, x
        group[y] = x
        size[x] += size[y]

    for a, b in AB:
        unite(a, b)

    # 出力
    if len(set([root(i) for i in range(1, N+1)])) == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    # 結果はYesかNo
    result = "Yes"

    # 並び順を保持するリスト
    order = []
    # 並び順を保持するリストを初期化
    for i in range(N):
        order.append(i+1)

    # 条件を保持するリスト
    condition = []
    # 条件を保持するリストを初期化
    for i in range(M):
        A, B = map(int, input().split())
        condition.append([A, B])

    # 条件を満たしているか判定
    for i in range(M):
        A = condition[i][0]
        B = condition[i][1]
        # 並び順のリストをループ
        for j in range(N):
            # 条件を満たしているか判定
            if order[j] == A:
                # 条件を満たしている場合、並び順のリストを入れ替え
                order[j] = B
            elif order[j] == B:
                # 条件を満たしている場合、並び順のリストを入れ替え
                order[j] = A

    # 並び順のリストをループ
    for i in range(N-1):
        # 条件を満たしているか判定
        if order[i] > order[i+1]:
            # 条件を満たしていない場合、結果をNoに変更
            result = "No"
            break

    # 結果を出力
    print(result)
