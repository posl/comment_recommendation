Synthesizing 10/10 solutions

=======
Suggestion 1

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

=======
Suggestion 2

def read():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    return N, X, Y

=======
Suggestion 3

def main():
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += ((X[i]-X[j])**2+(Y[i]-Y[j])**2)**0.5
    print(ans*N*2/N/N)

=======
Suggestion 4

def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    perm = [i for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += ((x[perm[i]] - x[perm[j]]) ** 2 + (y[perm[i]] - y[perm[j]]) ** 2) ** 0.5
    for i in range(2, N + 1):
        ans /= i
    print(ans)

=======
Suggestion 5

def distance(t1, t2):
    return ((t1[0]-t2[0])**2 + (t1[1]-t2[1])**2)**(1/2)

=======
Suggestion 6

def main():
    import sys
    from itertools import permutations
    input = sys.stdin.readline
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    ans = 0
    for p in permutations(range(N)):
        for i in range(N-1):
            ans += ((X[p[i]]-X[p[i+1]])**2+(Y[p[i]]-Y[p[i+1]])**2)**0.5
    print(ans/N)

=======
Suggestion 7

def main():
    N = int(input())
    town = []
    for i in range(N):
        x, y = map(int, input().split())
        town.append((x, y))
    from itertools import permutations
    perm = permutations(range(N))
    ans = 0
    for p in perm:
        for i in range(N-1):
            ans += ((town[p[i]][0]-town[p[i+1]][0])**2+(town[p[i]][1]-town[p[i+1]][1])**2)**(1/2)
    print(ans/N/math.factorial(N))

=======
Suggestion 8

def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    import itertools
    l = list(itertools.permutations(range(n)))
    ans = 0
    for i in l:
        for j in range(n-1):
            ans += ((xy[i[j]][0]-xy[i[j+1]][0])**2+(xy[i[j]][1]-xy[i[j+1]][1])**2)**0.5
    print(ans/len(l))

=======
Suggestion 9

def main():
    from itertools import permutations
    import math
    N = int(input())
    town = [list(map(int,input().split())) for _ in range(N)]
    path = list(permutations(range(N)))
    ans = 0
    for i in range(len(path)):
        for j in range(N-1):
            ans += math.sqrt((town[path[i][j]][0]-town[path[i][j+1]][0])**2+(town[path[i][j]][1]-town[path[i][j+1]][1])**2)
    print(ans/len(path))

=======
Suggestion 10

def input(): return sys.stdin.readline().rstrip()
