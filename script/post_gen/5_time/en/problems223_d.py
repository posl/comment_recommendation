Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = [0] * N
    for i in range(N):
        ans[i] = i + 1
    for i in range(M):
        if ans[A[i] - 1] > ans[B[i] - 1]:
            ans[A[i] - 1], ans[B[i] - 1] = ans[B[i] - 1], ans[A[i] - 1]
    for i in range(N - 1):
        if ans[i] > ans[i + 1]:
            print(-1)
            exit()
    print(" ".join(map(str, ans)))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = [0] * N
    for i in range(N):
        ans[i] = i + 1
    for i in range(M):
        if ans[A[i] - 1] > ans[B[i] - 1]:
            ans[A[i] - 1], ans[B[i] - 1] = ans[B[i] - 1], ans[A[i] - 1]
    print(*ans)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.reverse()
    b.reverse()
    p = []
    for i in range(n):
        p.append(i+1)
    for i in range(m):
        if p.index(a[i]) > p.index(b[i]):
            p[p.index(a[i])], p[p.index(b[i])] = p[p.index(b[i])], p[p.index(a[i])]
    print(*p)

=======
Suggestion 4

def solve():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a = a[::-1]
    b = b[::-1]

    ans = [-1] * (n + 1)
    for i in range(m):
        if ans[a[i]] == -1 and ans[b[i]] == -1:
            ans[a[i]] = b[i]
            ans[b[i]] = a[i]
        elif ans[a[i]] == -1:
            ans[a[i]] = b[i]
        elif ans[b[i]] == -1:
            ans[b[i]] = a[i]
        else:
            if ans[a[i]] != b[i] or ans[b[i]] != a[i]:
                print(-1)
                exit()

    for i in range(1, n + 1):
        if ans[i] == -1:
            ans[i] = i

    print(*ans[1:])

=======
Suggestion 5

def solve(N, M, A, B):
    # write code here
    pass

N, M = map(int, input().split())
A = []
B = []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = solve(N, M, A, B)
print(ans)

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[0])
    AB.sort(key=lambda x: x[1])
    print(' '.join(map(str, [AB[i][0] for i in range(M)])))

=======
Suggestion 7

def solve():
    n,m = map(int,input().split())
    ans = [-1]*n
    for _ in range(m):
        a,b = map(int,input().split())
        if ans[a-1]==-1 and ans[b-1]==-1:
            ans[a-1]=b
            ans[b-1]=a
        elif ans[a-1]==-1:
            ans[a-1]=b
            ans[b-1]=a
        elif ans[b-1]==-1:
            ans[b-1]=a
            ans[a-1]=b
        else:
            if ans[a-1]==b:
                continue
            else:
                print(-1)
                return
    print(*ans)
solve()

=======
Suggestion 8

def solve(N, M, AB):
    ans = [-1] * N
    for i in range(M):
        a = AB[i][0]
        b = AB[i][1]
        if ans[a-1] == -1 and ans[b-1] == -1:
            ans[a-1] = b
            ans[b-1] = a
        elif ans[a-1] == -1:
            ans[a-1] = b
        elif ans[b-1] == -1:
            ans[b-1] = a
        else:
            if ans[a-1] != b or ans[b-1] != a:
                return [-1]
    return ans

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
ans = solve(N, M, AB)

=======
Suggestion 9

def is_cycle(graph, start):
    seen = set()
    to_visit = [start]
    while to_visit:
        node = to_visit.pop()
        if node in seen:
            return True
        seen.add(node)
        to_visit.extend(graph[node])
    return False

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
for i in range(n):
    if is_cycle(graph, i):
        print(-1)
        break
else:
    print(*sorted(range(1, n + 1), key=lambda x: graph[x - 1]))

=======
Suggestion 10

def main():
    pass
