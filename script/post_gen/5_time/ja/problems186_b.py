Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]

    min_a = min([min(a[i]) for i in range(h)])

    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a

    print(ans)

=======
Suggestion 2

def solve():
    H,W = map(int,input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int,input().split())))

    minA = 101
    for i in range(H):
        for j in range(W):
            minA = min(minA,A[i][j])

    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - minA

    print(ans)

=======
Suggestion 3

def solve():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))

    minv = 100
    for i in range(H):
        for j in range(W):
            minv = min(minv, A[i][j])

    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - minv

    print(ans)

=======
Suggestion 4

def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_a = 100
    for i in range(H):
        for j in range(W):
            min_a = min(min_a, A[i][j])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min_a
    print(ans)
solve()

=======
Suggestion 5

def solve():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    min_A = 100
    for i in range(H):
        for j in range(W):
            min_A = min(min_A, A[i][j])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min_A
    print(ans)

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))

    min_a = 100
    for i in range(h):
        for j in range(w):
            if a[i][j] < min_a:
                min_a = a[i][j]

    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a

    print(ans)

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    min_a = 101
    for i in range(h):
        for j in range(w):
            min_a = min(min_a, a[i][j])
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a
    print(ans)

=======
Suggestion 8

def problems186_b():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    min_a = min(min(a))
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a
    print(ans)

=======
Suggestion 9

def get_ints(): return map(int, input().split())

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_A = min([min(A[i]) for i in range(H)])
    print(sum([sum(A[i]) - min_A * W for i in range(H)]))
