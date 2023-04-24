Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    # city iからcity jに行けるかどうかの行列を作る
    # ここで、行列の要素は、iからjに行ける道の数
    # なお、iからjに行ける道がないときは、0とする
    # また、iからiに行ける道は、0とする
    # この行列を途中で更新していく
    # まず、iからjに行ける道があるとき、iからkに行けるかどうかの行列を更新する
    # すると、iからjに行ける道があるとき、iからkに行けるかどうかの行列が更新される
    # これを、kがN以下の数を取りうるまで繰り返す
    # そして、iからjに行ける道があるとき、iからkに行けるかどうかの行列の要素の和を求める
    # これが、iからjに行ける道の数になる
    # この行列の要素の和を求める
    # この行列の要素の和が、iからjに行ける道の数になる
    # この行列の要素の和を求める
    # この行列の要素の和が、iからjに行ける道の数になる
    # この行列の要素の

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    ans = n * (n - 1) - m
    for i in range(m):
        for j in range(m):
            if a[i] == a[j] and b[i] == b[j]:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    road = [[0] * N for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        road[A - 1][B - 1] = 1
    ans = 0
    for i in range(N):
        for j in range(N):
            if road[i][j] == 1:
                for k in range(N):
                    if road[j][k] == 1:
                        road[i][k] = 1
    for i in range(N):
        for j in range(N):
            if road[i][j] == 1:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N * N)
        return
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
    ans = 0
    for i in range(N):
        stack = [i]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for next_node in graph[node]:
                stack.append(next_node)
        ans += len(visited)
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = N * (N - 1)
    for a, b in AB:
        if a > b:
            a, b = b, a
        ans -= (N - a) * (N - b)
    print(ans)

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    A=[]
    B=[]
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    if M==0:
        print(N*N)
        return
    if M==N*(N-1)//2:
        print(0)
        return
    A = set(A)
    B = set(B)
    A = list(A)
    B = list(B)
    A.sort()
    B.sort()
    A = [0]+A
    B = [0]+B
    A.append(N+1)
    B.append(N+1)
    ans = 0
    for i in range(len(A)-1):
        for j in range(len(B)-1):
            if A[i+1]-A[i]==1 and B[j+1]-B[j]==1:
                continue
            else:
                ans += (A[i+1]-A[i])*(B[j+1]-B[j])
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab.sort()
    ans = 0
    for i in range(m):
        a, b = ab[i]
        for j in range(i + 1, m):
            c, d = ab[j]
            if a <= c <= b:
                if b <= d:
                    ans += (b - c) * (b - c + 1) // 2
                else:
                    ans += (d - c) * (d - c + 1) // 2
            elif c <= a <= d:
                if d <= b:
                    ans += (d - a) * (d - a + 1) // 2
                else:
                    ans += (b - a) * (b - a + 1) // 2
    print(ans)

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    D = [0] * N
    for i in range(M):
        a, b = map(int, input().split())
        D[a-1] += 1
        D[b-1] += 1
    ans = 0
    for i in range(N):
        ans += D[i]*(D[i]-1)//2
    print(ans)

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    ans = 0
    for i in range(M):
        g = [[] for _ in range(N)]
        for j in range(M):
            if i == j:
                continue
            a,b = AB[j]
            a,b = a-1,b-1
            g[a].append(b)
        for j in range(N):
            q = [j]
            v = [0]*N
            while q:
                x = q.pop()
                for y in g[x]:
                    if v[y]:
                        continue
                    v[y] = 1
                    q.append(y)
            ans += sum(v)
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    # 0-index
    AB = [[a - 1, b - 1] for a, b in AB]

    # count the number of cities that can be reached from city i
    # (directly or indirectly)
    reach = [0] * N
    for a, b in AB:
        reach[a] += 1
        reach[b] += 1

    # count the number of pairs (a, b) where a can reach b
    reach_to = [0] * N
    for a, b in AB:
        if reach[a] < reach[b]:
            reach_to[a] += 1
        else:
            reach_to[b] += 1

    ans = sum(r * (r - 1) for r in reach_to)
    print(ans)
