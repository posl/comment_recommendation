Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = [0] * (n - 1)
    b = [0] * (n - 1)
    for i in range(n - 1):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    if a[0] == 1 and b[0] == n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = int(input())
    a = [0] * (n-1)
    b = [0] * (n-1)
    for i in range(n-1):
        a[i], b[i] = map(int, input().split())
    #print(a)
    #print(b)
    #print(set(a))
    #print(set(b))
    #print(set(a) & set(b))
    #print(set(a) | set(b))
    #print(set(a) ^ set(b))
    if len(set(a) & set(b)) == 1 and len(set(a) | set(b)) == n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n-1):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    if a[0] == 1 and n == b[-1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    if a[0] == 1:
        if a == b:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 5

def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    a.sort()
    b.sort()
    if a[0] == 1 and b.count(N) == N-1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n-1):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    print('Yes' if len(set(a)) == 1 or len(set(b)) == 1 else 'No')

=======
Suggestion 7

def star_graph():
    N = int(input())
    graph = {}
    for i in range(N-1):
        a,b = map(int, input().split())
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)
    for node in graph:
        if len(graph[node]) == N-1:
            print("Yes")
            return
    print("No")
    return

star_graph()

=======
Suggestion 8

def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        edges.append(list(map(int, input().split())))
    #print(edges)
    #print(len(edges))
    #print(len(set(edges)))
    if len(edges) != len(set(edges)):
        print("No")
    else:
        print("Yes")

=======
Suggestion 9

def isStar(n, a, b):
    if n-1 != len(a) or n-1 != len(b):
        return False
    if n == 3:
        return True
    c = [0 for i in range(n)]
    for i in range(n-1):
        c[a[i]-1] += 1
        c[b[i]-1] += 1
    for i in range(n):
        if c[i] == n-1:
            return True
    return False

=======
Suggestion 10

def check_star(n, edges):
    # check if all nodes except one have degree 1
    if len(edges) != n-1:
        return False
    degree = [0]*n
    for a, b in edges:
        degree[a-1] += 1
        degree[b-1] += 1
    if degree.count(1) != n-1:
        return False
    # check if the remaining node has degree n-1
    if degree.count(n-1) != 1:
        return False
    return True
