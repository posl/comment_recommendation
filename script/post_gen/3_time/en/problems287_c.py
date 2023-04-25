Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print("No")
        return
    for _ in range(M):
        u, v = map(int, input().split())
        if abs(u - v) > 1:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print('No')
        return
    u = [0] * M
    v = [0] * M
    for i in range(M):
        u[i], v[i] = map(int, input().split())
    u.sort()
    v.sort()
    if u[0] == 1 and v[-1] == N:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    if M == N - 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n,m=map(int,input().split())
    if m!=n-1:
        print("No")
        return
    s=set()
    for _ in range(m):
        u,v=map(int,input().split())
        s.add(u)
        s.add(v)
    if len(s)!=n:
        print("No")
        return
    print("Yes")
    return

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    if M != N-1:
        print("No")
        return
    edges = []
    for _ in range(M):
        edges.append(list(map(int, input().split())))
    if len(edges) != len(set([tuple(edge) for edge in edges])):
        print("No")
        return
    if len(set([edge[0] for edge in edges])) > 1 and len(set([edge[1] for edge in edges])) > 1:
        print("No")
        return
    print("Yes")
    return

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    if N == M:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    if m != n-1:
        print("No")
        return
    for i in range(m):
        u,v = map(int,input().split())
        if u == 1 or v == 1:
            continue
        print("No")
        return
    print("Yes")

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print("No")
    else:
        print("Yes")

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    if m != n-1:
        print("No")
        return
    nodes = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        nodes[u-1] += 1
        nodes[v-1] += 1
    if max(nodes) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    if m==n-1:
        print('Yes')
    else:
        print('No')
