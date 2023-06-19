Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].append(b-1)
    ans = []
    from collections import deque
    q = deque()
    for i in range(n):
        if not g[i]:
            q.append(i)
    while q:
        v = q.popleft()
        ans.append(v)
        for i in range(n):
            if v in g[i]:
                g[i].remove(v)
                if not g[i]:
                    q.append(i)
    if len(ans) != n:
        print(-1)
    else:
        print(*[x+1 for x in ans])

solve()

=======
Suggestion 3

def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    print(A)
    print(B)
    print("Hello World!")

=======
Suggestion 4

def solve():
    pass

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #print(A)
    #print(B)

    # A_i在P中比B_i早出现。
    # 1. A_i, B_i都在P中
    # 2. A_i在P中，B_i不在P中
    # 3. A_i不在P中，B_i在P中
    # 4. A_i, B_i都不在P中
    # 1. A_i, B_i都在P中
    # 2. A_i在P中，B_i不在P中
    # 3. A_i不在P中，B_i在P中
    # 4. A_i, B_i都不在P中
    # 1. A_i, B_i都在P中
    # 2. A_i在P中，B_i不在P中
    # 3. A_i不在P中，B_i在P中
    # 4. A_i, B_i都不在P中
    # 1. A_i, B_i都在P中
    # 2. A_i在P中，B_i不在P中
    # 3. A_i不在P中，B_i在P中
    # 4. A_i, B_i都不在P中
    # 1. A_i, B_i都在P中
    # 2. A_i在P中，B_i不在P中
    # 3. A_i不在P中，B_i在P中
    # 4. A_i, B_i都不在P中
    # 1. A_i, B_i都在P中
    # 2. A_i在P中，B_i不在P中
    # 3. A_i不在P中，B_i在P中
    # 4. A_i, B_i都不在P中

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    # 逆向思维，从后往前找，即从N开始
    ans = [i for i in range(1,n+1)]
    for i in range(m):
        if ans.index(a[m-1-i]) < ans.index(b[m-1-i]):
            continue
        else:
            ans.remove(a[m-1-i])
            ans.insert(ans.index(b[m-1-i]), a[m-1-i])

    print(*ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for _ in range(m):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    ans = [0] * n
    for i in range(n):
        ans[i] = i + 1
    for i in range(m):
        if ans[a[i] - 1] > ans[b[i] - 1]:
            ans[a[i] - 1], ans[b[i] - 1] = ans[b[i] - 1], ans[a[i] - 1]
    print(*ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    p = list(range(1, N+1))
    for i in range(M):
        if A[i] > B[i]:
            A[i], B[i] = B[i], A[i]
    for i in range(M):
        if A[i] == p[0] and B[i] == p[1]:
            p[0], p[1] = p[1], p[0]
            break
    for i in range(2, N):
        for j in range(M):
            if A[j] == p[i]:
                if B[j] == p[i-1]:
                    p[i-1], p[i] = p[i], p[i-1]
                    break
                elif B[j] == p[i-2]:
                    p[i-2], p[i-1] = p[i-1], p[i-2]
                    p[i-1], p[i] = p[i], p[i-1]
                    break
    print(*p)

=======
Suggestion 9

def solve():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # 逆向きに解く
    # ある数値が出現する回数を数える
    # ある数値より小さい数値の出現回数を数える
    # ある数値より大きい数値の出現回数を数える
    count = [0] * N
    smaller = [0] * N
    bigger = [0] * N
    for i in range(M):
        count[B[i]-1] += 1
        if A[i] < B[i]:
            smaller[B[i]-1] += 1
        if A[i] > B[i]:
            bigger[B[i]-1] += 1

    # 答えを格納する配列
    ans = []
    # ある数値を出現させるかどうかを決める
    # ある数値より小さい数値が出現していない
    # かつ、ある数値より大きい数値が出現していない
    # ある数値より小さい数値の出現回数を減らす
    # ある数値より大きい数値の出現回数を増やす
    for i in range(N):
        if smaller[i] == 0 and bigger[i] == 0:
            ans.append(i+1)
            for j in range(N):
                if smaller[j] > 0:
                    smaller[j] -= 1
                if bigger[j] > 0:
                    bigger[j] += 1

    # 答えを出力する
    if len(ans) == N:
        print(*ans)
    else:
        print(-1)
