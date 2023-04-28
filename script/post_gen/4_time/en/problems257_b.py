Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    B = [0] * N
    for i in range(Q):
        B[L[i]-1] += 1
    for i in range(N):
        if K - Q + B[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))

    score = [0] * N
    for i in range(Q):
        score[L[i]-1] += 1

    for i in range(N):
        if K - Q + score[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = [int(input()) for i in range(Q)]
    B = [0] * N
    for i in range(Q):
        B[L[i] - 1] += 1
    for i in range(N):
        if K - Q + B[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = [int(input()) for i in range(q)]
    p = [0] * n
    for i in range(k):
        p[a[i] - 1] += 1
    for i in range(q):
        p[l[i] - 1] += 1
    for i in range(n):
        if p[i] > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def main():
    n, k, q = map(int, input().split())
    a = [int(i) for i in input().split()]
    l = [int(i) for i in input().split()]
    for i in range(k):
        c = 0
        for j in range(q):
            if a[i] == l[j]:
                c += 1
        if c > q - k:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def solve():
    n, k, q = map(int, input().split())
    a = [int(i) for i in input().split()]
    l = [int(i) for i in input().split()]
    b = [0] * n
    for i in range(q):
        b[l[i] - 1] += 1
    for i in range(n):
        if a[i] - k + sum(b[:i]) > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    # input
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = [int(input()) for i in range(q)]

    # compute
    points = [0] * n
    for i in range(k):
        points[a[i]-1] += 1
    for i in range(q):
        points[l[i]-1] += 1

    # output
    for i in range(n):
        if points[i] > q:
            print('Yes')
        else:
            print('No')

=======
Suggestion 8

def main():
    N,K,Q = map(int,input().split())
    A = list(map(int,input().split()))
    L = [int(input()) for i in range(Q)]
    ans = [0]*N
    for i in L:
        ans[i-1] += 1
    for i in range(N):
        if K - Q + ans[i] > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 9

def move_right(pieces, i):
    if i == len(pieces):
        return pieces
    if pieces[i] == len(pieces):
        return move_right(pieces, i + 1)
    if pieces[i] < len(pieces) and pieces[i] + 1 in pieces:
        return move_right(pieces, i + 1)
    pieces[i] += 1
    return move_right(pieces, i + 1)

N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

pieces = [0] * N
for i in range(K):
    pieces[A[i] - 1] = 1

for i in range(Q):
    pieces = move_right(pieces, L[i] - 1)

for i in range(N):
    if pieces[i] == 0:
        print("No")
    else:
        print("Yes")
