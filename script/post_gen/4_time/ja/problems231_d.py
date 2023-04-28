Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    if M == 0:
        print('Yes')
        return
    A.sort()
    B.sort()
    if A[0] == 1 and B[-1] == N:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    print('Yes' if len(set(A + B)) == N else 'No')

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    A.sort()
    B.sort()
    if A[0] == 1 and B[-1] == N:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def solve():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    if a[0] == 1 and b[-1] == n:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

=======
Suggestion 5

def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if A[0] == 1 and B[-1] == N:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = [0] * (m)
    b = [0] * (m)
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    if a[0] == 1 and b[m-1] == n:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')

=======
Suggestion 7

def main():
    # input
    N, M = map(int, input().split())
    ABs = [list(map(int, input().split())) for _ in range(M)]

    # compute
    ABs.sort(key=lambda x: x[0])
    ABs.sort(key=lambda x: x[1])

    # output
    for i in range(M-1):
        if ABs[i][1] == ABs[i+1][0]:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    min = 0
    max = 0
    for i in range(m):
        a,b = map(int,input().split())
        if a < min or min == 0:
            min = a
        if a > max:
            max = a
        if b < min:
            min = b
        if b > max:
            max = b
    if min == 1 and max == n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    N, M = map(int, input().split())

    # 隣り合っている人のリストを作成
    people = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        people[A-1].append(B-1)
        people[B-1].append(A-1)

    # 隣り合っている人のリストの中で、最も長いものを探す
    # この長さが N-1 ならば、全ての条件を満たすことができる
    # そうでなければ、満たすことができない
    max_len = 0
    for p in people:
        if len(p) > max_len:
            max_len = len(p)

    if max_len == N-1:
        print('Yes')
    else:
        print('No')
