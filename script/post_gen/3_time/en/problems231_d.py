Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(2 ** N):
        flag = True
        for j in range(M):
            if (i >> (A[j] - 1)) % 2 == 1 and (i >> (B[j] - 1)) % 2 == 1:
                flag = False
                break
        if flag:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A = [a - 1 for a in A]
    B = [b - 1 for b in B]
    G = [[] for _ in range(N)]
    for i in range(M):
        G[A[i]].append(B[i])
        G[B[i]].append(A[i])
    used = [False] * N
    def dfs(v):
        used[v] = True
        for nv in G[v]:
            if used[nv]:
                continue
            dfs(nv)
    cnt = 0
    for i in range(N):
        if used[i]:
            continue
        dfs(i)
        cnt += 1
    print("Yes" if cnt == 1 else "No")

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print("Yes" if solve(N, M, A, B) else "No")

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    # ????????????

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

    # 1. 2つの条件を満たすことは可能か？
    # 2. 3つ以上の条件を満たすことは可能か？
    # 3. 2つの条件を満たすときのみ条件を満たすことは可能か？
    # 4. 3つ以上の条件を満たすときのみ条件を満たすことは可能か？

    # 1. 2つの条件を満たすことは可能か？
    # 2つの条件を満たすときのみ条件を満たすことは可能か？
    # 2つの条件を満たすときのみ条件を満たすことは可能か？
    # 3つ以上の条件を満たすときのみ条件を満たすことは可能か？
    # 3つ以上の条件を満たすときのみ条件を満たすことは可能か？

    # 1. 2つの条件を満たすことは可能か？
    # 2つの条件を満たすときのみ条件を満たすことは可能か？
    # 3つ以上の条件を満たすときのみ条件を満たすことは可能か？
    # 4つ以上の条件を満たすときのみ条件を満たすことは可能か？

    # 1. 2つの条件を満たすことは可能か？
    # 2つの条件を満たすときのみ条件を満たすことは可能か？
    # 3つ以上の条件を満たすときのみ条件を満たすことは可能か？
    # 4つ以上の条件を満たすときのみ条件を満たす

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    if M == 0:
        print("Yes")
        return
    for i in range(N):
        if len(G[i]) == 0:
            print("No")
            return
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if len(set(G[i]) & set(G[j])) == 0:
                print("No")
                return
    print("Yes")
main()

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    edges = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)

    def dfs(v):
        visited[v] = True
        for u in edges[v]:
            if visited[u]:
                continue
            dfs(u)

    visited = [False] * n
    dfs(0)
    print("Yes" if all(visited) else "No")

=======
Suggestion 8

def union_find(n):
    par = list(range(n))
    size = [1] * n
    def root(x):
        if par[x] == x:
            return x
        else:
            par[x] = root(par[x])
            return par[x]
    def same(x, y):
        return root(x) == root(y)
    def unite(x, y):
        x = root(x)
        y = root(y)
        if x == y:
            return
        if size[x] < size[y]:
            x, y = y, x
        par[y] = x
        size[x] += size[y]
    return root, same, unite

n, m = map(int, input().split())
root, same, unite = union_find(n)
for _ in range(m):
    a, b = map(int, input().split())
    unite(a-1, b-1)
print('Yes' if len(set(root(i) for i in range(n))) == 1 else 'No')

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for i in range(M)]
    AB.sort(key=lambda x:x[0])
    AB.sort(key=lambda x:x[1])
    ans = "Yes"
    for i in range(M-1):
        if AB[i][1] == AB[i+1][1]:
            ans = "No"
            break
    print(ans)

=======
Suggestion 10

def main():
    #input
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for i in range(M)]
    #initialization
    #1~Nの人がいると考える
    #1~Nの人がどこにいるかを保持するリスト
    #0のときはいないとする
    where = [0 for i in range(N+1)]
    #1~Nの人がどこにいるかを保持するリスト
    #0のときはいないとする
    where = [0 for i in range(N+1)]
    #1~Nの人が何人いるかを保持するリスト
    #0のときはいないとする
    how_many = [0 for i in range(N+1)]
    #1~Nの人がいるところの人数を保持するリスト
    #0のときはいないとする
    how_many_people = [0 for i in range(N+1)]
    #1~Nの人がいるところの人数を保持するリスト
    #0のときはいないとする
    how_many_people = [0 for i in range(N+1)]
    #1~Nの人がいるところの人数を保持するリスト
    #0のときはいないとする
    how_many_people = [0 for i in range(N+1)]
    #1~Nの人がいるところの人数を保持するリスト
    #0のときはいないとする
    how_many_people = [0 for i in range(N+1)]
    #1~Nの人がいるところの人数を保持するリスト
    #0のときはいないとする
    how_many_people = [0 for i in range(N+1)]
    #1~Nの人がいるところの人数を保持するリスト
    #0のときはいないとする
    how_many_people = [0 for i in range(N+1)]
