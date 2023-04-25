Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    for i in range(N):
        print(A.index(A[i]) + 1, B.index(B[i]) + 1)

=======
Suggestion 2

def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    h = [0] * (H + 1)
    w = [0] * (W + 1)
    for i in range(N):
        h[A[i]] = 1
        w[B[i]] = 1
    for i in range(1, H + 1):
        h[i] += h[i - 1]
    for i in range(1, W + 1):
        w[i] += w[i - 1]
    for i in range(N):
        print(h[A[i]], w[B[i]])

=======
Suggestion 3

def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = list(set(A))
    B = list(set(B))
    A.sort()
    B.sort()
    for i in range(N):
        print(A.index(A[i]) + 1, B.index(B[i]) + 1)

=======
Suggestion 4

def main():
    H, W, N = map(int, input().split())
    x = []
    y = []
    for _ in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)

    x = list(set(x))
    y = list(set(y))
    x.sort()
    y.sort()

    for i in range(N):
        a, b = map(int, input().split())
        print(x.index(a) + 1, y.index(b) + 1)

=======
Suggestion 5

def main():
    H, W, N = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = [a for a, b in AB]
    B = [b for a, b in AB]
    A.sort()
    B.sort()
    d = {a: i for i, a in enumerate(A)}
    e = {b: i for i, b in enumerate(B)}
    for a, b in AB:
        print(d[a] + 1, e[b] + 1)

=======
Suggestion 6

def main():
    H, W, N = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(N)]
    cards.sort(key=lambda x: x[0])
    cards.sort(key=lambda x: x[1])
    row = 1
    col = 1
    row_list = []
    col_list = []
    for i in range(N):
        while row < cards[i][0]:
            row_list.append(row)
            row += 1
        while col < cards[i][1]:
            col_list.append(col)
            col += 1
        row_list.append(cards[i][0])
        col_list.append(cards[i][1])
        row += 1
        col += 1
    while row <= H:
        row_list.append(row)
        row += 1
    while col <= W:
        col_list.append(col)
        col += 1

    for i in range(N):
        print(row_list[i], col_list[i])

=======
Suggestion 7

def main():
    H, W, N = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    A, B = zip(*AB)
    A = list(A)
    B = list(B)
    A.sort()
    B.sort()
    A = [i for i, v in enumerate(A)]
    B = [i for i, v in enumerate(B)]
    for i in range(N):
        print(A[i]+1, B[i]+1)

=======
Suggestion 8

def main():
    H, W, N = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(N)]
    cards.sort(key = lambda x: x[0])
    cards.sort(key = lambda x: x[1])
    cards.sort(key = lambda x: x[0] + x[1])
    cards.sort(key = lambda x: x[0] * x[1])
    cards.sort(key = lambda x: x[0] + x[1])

    for i in range(N):
        print(cards[i][0], cards[i][1])

=======
Suggestion 9

def main():
    H, W, N = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(N)]
    cards.sort(key=lambda x:x[0]*W+x[1])
    cards.sort(key=lambda x:x[0])
    for i in range(N):
        print(cards[i][0], cards[i][1])
