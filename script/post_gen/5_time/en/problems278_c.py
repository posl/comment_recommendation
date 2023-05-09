Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    follow = set()
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow.add((a, b))
        elif t == 2:
            follow.discard((a, b))
        else:
            if (a, b) in follow and (b, a) in follow:
                print('Yes')
            else:
                print('No')

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    follow = [set() for _ in range(n)]
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a-1].add(b-1)
        elif t == 2:
            follow[a-1].discard(b-1)
        else:
            if a-1 in follow[b-1] and b-1 in follow[a-1]:
                print('Yes')
            else:
                print('No')
    return

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    follow = [[False] * n for _ in range(n)]
    for _ in range(q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            follow[a][b] = True
        elif t == 2:
            follow[a][b] = False
        else:
            if follow[a][b]:
                print('Yes')
            else:
                print('No')

=======
Suggestion 4

def main():
    N,Q = map(int, input().split())
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    # print(N, Q, T, A, B)
    # print(N, Q)
    # print(T)
    # print(A)
    # print(B)
    # print("")

    # 1 1 2
    # 3 1 2
    # 1 2 1
    # 3 1 2
    # 1 2 3
    # 1 3 2
    # 3 1 3
    # 2 1 2
    # 3 1 2

    # 1 1 2
    # 1 2 1
    # 3 1 2
    # 1 1 2
    # 1 1 2
    # 1 1 2
    # 2 1 2
    # 3 1 2

    # 3 1 6
    # 3 5 4
    # 1 6 1
    # 3 1 7
    # 3 8 4
    # 1 1 6
    # 2 4 3
    # 1 6 5
    # 1 5 6
    # 1 1 8
    # 1 8 1
    # 2 3 10
    # 1 7 6
    # 3 5 6
    # 1 6 7
    # 3 6 7
    # 1 9 5
    # 3 8 6
    # 3 3 8
    # 2 6 9
    # 1 7 1
    # 3 10 8
    # 2 9 2
    # 1 10 9
    # 2 6 10
    # 2 6 8
    # 3 1 6
    #

=======
Suggestion 5

def main():
    n, q = map(int, input().split())
    follow = [[] for _ in range(n)]
    for _ in range(q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            follow[a].append(b)
        elif t == 2:
            if b in follow[a]:
                follow[a].remove(b)
        else:
            if b in follow[a] and a in follow[b]:
                print('Yes')
            else:
                print('No')

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    follow = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a-1][b-1] = 1
        elif t == 2:
            follow[a-1][b-1] = 0
        else:
            if follow[a-1][b-1] == 1:
                print("Yes")
            else:
                print("No")

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    follow = [[False for _ in range(N)] for _ in range(N)]
    for _ in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            follow[A - 1][B - 1] = True
        elif T == 2:
            follow[A - 1][B - 1] = False
        else:
            if follow[A - 1][B - 1]:
                print('Yes')
            else:
                print('No')

=======
Suggestion 8

def solve(N, Q, T, A, B):
    pass

N, Q = map(int, input().split())
T = [0] * Q
A = [0] * Q
B = [0] * Q
for i in range(Q):
    T[i], A[i], B[i] = map(int, input().split())

print(solve(N, Q, T, A, B))

=======
Suggestion 9

def read_ints():
    return list(map(int, input().split()))

=======
Suggestion 10

def main():
    n, q = map(int, input().split())
    # print(n, q)
    follow = [False] * (n * n)
    # print(follow)

    def follow_check(a, b):
        if a == b:
            return False
        if a > b:
            a, b = b, a
        return follow[a * n + b]

    def follow_set(a, b):
        if a == b:
            return
        if a > b:
            a, b = b, a
        follow[a * n + b] = True

    def follow_unset(a, b):
        if a == b:
            return
        if a > b:
            a, b = b, a
        follow[a * n + b] = False

    for i in range(q):
        t, a, b = map(int, input().split())
        # print(t, a, b)
        if t == 1:
            follow_set(a, b)
        elif t == 2:
            follow_unset(a, b)
        elif t == 3:
            if follow_check(a, b):
                print('Yes')
            else:
                print('No')
