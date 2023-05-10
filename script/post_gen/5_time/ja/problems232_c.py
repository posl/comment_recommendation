Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    c = [list(map(int, input().split())) for _ in range(m)]
    if m == 0:
        print("Yes")
        return
    a.sort()
    c.sort()
    for i in range(m):
        if a[i][1] != c[i][1]:
            print("No")
            return
    print("Yes")

main()

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    cd = [list(map(int, input().split())) for _ in range(m)]

    def check(p):
        for a, b in ab:
            if (p.index(a) < p.index(b)) != (a in p[:p.index(b)]):
                return False
        for c, d in cd:
            if (p.index(c) < p.index(d)) != (c in p[:p.index(d)]):
                return False
        return True

    def dfs(s, p):
        if len(p) == n:
            if check(p):
                print('Yes')
                exit()
            return
        for i in range(s, n + 1):
            dfs(i + 1, p + [i])

    dfs(1, [])
    print('No')

=======
Suggestion 3

def chk_same_shape(n, m, list_ab, list_cd):
    if m == 0:
        return 'Yes'
    list_ab.sort()
    list_cd.sort()
    if list_ab == list_cd:
        return 'Yes'
    else:
        return 'No'

n, m = map(int, input().split())
list_ab = []
list_cd = []
for i in range(m):
    a, b = map(int, input().split())
    list_ab.append([a, b])
for i in range(m):
    c, d = map(int, input().split())
    list_cd.append([c, d])

print(chk_same_shape(n, m, list_ab, list_cd))

=======
Suggestion 4

def check(a, b, p):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a[j] and b[i] != b[j]:
                return False
            if a[i] != a[j] and b[i] == b[j]:
                return False
            if a[i] == a[j] and b[i] == b[j]:
                if p[i] != p[j]:
                    return False
    return True


n, m = map(int, input().split())
a = []
b = []
c = []
d = []
for i in range(m):
    tmp_a, tmp_b = map(int, input().split())
    a.append(tmp_a)
    b.append(tmp_b)
for i in range(m):
    tmp_c, tmp_d = map(int, input().split())
    c.append(tmp_c)
    d.append(tmp_d)

p = [i for i in range(1, n+1)]
ans = "No"
for i in range(2**n):
    tmp = []
    for j in range(n):
        if (i >> j) & 1:
            tmp.append(p[j])
    if len(tmp) == n:
        if check(a, b, tmp) and check(c, d, tmp):
            ans = "Yes"
print(ans)

=======
Suggestion 5

def solve():
    # ===CODE===
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)

    for i in range(2**N):
        P = []
        for j in range(N):
            if ((i >> j) & 1):
                P.append(j+1)
        if len(P) != N:
            continue
        # print(P)
        # print(i)
        flag = True
        for j in range(M):
            if (A[j] in P) and (B[j] in P):
                pass
            elif (C[j] in P) and (D[j] in P):
                pass
            else:
                flag = False
                break
        if flag:
            print("Yes")
            return
    print("No")

=======
Suggestion 6

def dfs(i, n, m, a, b, c, d, visited):
  if i == n:
    return True
  for j in range(n):
    if visited[j]:
      continue
    if a[i] == c[j] and b[i] == d[j]:
      visited[j] = True
      if dfs(i + 1, n, m, a, b, c, d, visited):
        return True
      visited[j] = False
  return False

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)

    if M == 0:
        print("Yes")
        return

    for i in range(1 << N):
        P = []
        for j in range(N):
            if i & (1 << j):
                P.append(j + 1)
        if len(P) != N:
            continue
        if check(A, B, C, D, P):
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]

    def make_graph(AB):
        graph = [[] for _ in range(N)]
        for a, b in AB:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        return graph

    def dfs(graph, v, visited):
        visited[v] = True

        for nv in graph[v]:
            if visited[nv]:
                continue
            dfs(graph, nv, visited)

    def is_connected(graph):
        visited = [False] * N
        dfs(graph, 0, visited)
        return all(visited)

    def solve():
        AB_graph = make_graph(AB)
        CD_graph = make_graph(CD)

        if not is_connected(AB_graph) or not is_connected(CD_graph):
            return False

        AB_degrees = [len(v) for v in AB_graph]
        CD_degrees = [len(v) for v in CD_graph]
        return sorted(AB_degrees) == sorted(CD_degrees)

    if solve():
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def check(a,b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

=======
Suggestion 10

def check(n, m, a, b, c, d):
    if m == 0:
        return True
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                continue
            if i in a and j in a:
                if not (a.index(i) == a.index(j) and b.index(i) == b.index(j)):
                    continue
            if i in c and j in c:
                if not (c.index(i) == c.index(j) and d.index(i) == d.index(j)):
                    continue
            if i in a and j in c:
                if not (a.index(i) == c.index(j) and b.index(i) == d.index(j)):
                    continue
            if i in c and j in a:
                if not (c.index(i) == a.index(j) and d.index(i) == b.index(j)):
                    continue
            if i in a and j in b:
                if not (a.index(i) == b.index(j) and b.index(i) == a.index(j)):
                    continue
            if i in c and j in d:
                if not (c.index(i) == d.index(j) and d.index(i) == c.index(j)):
                    continue
            if i in b and j in a:
                if not (b.index(i) == a.index(j) and a.index(i) == b.index(j)):
                    continue
            if i in d and j in c:
                if not (d.index(i) == c.index(j) and c.index(i) == d.index(j)):
                    continue
            if i in b and j in b:
                if not (b.index(i) == b.index(j) and a.index(i) == a.index(j)):
                    continue
            if i in d and j in d:
                if not (d.index(i) == d.index(j) and c.index(i) == c.index(j)):
                    continue
            if i in b and j in d:
                if not (b.index(i) == d.index(j) and a.index(i) == c.index(j)):
                    continue
            if i in d and j in b:
                if not (
