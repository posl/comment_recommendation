Synthesizing 10/10 solutions

=======
Suggestion 1

def get_min(a, b):
    if a > b:
        return b
    else:
        return a

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    min_a = min([min(a) for a in A])
    print(sum([sum(a) for a in A]) - min_a * H * W)

=======
Suggestion 3

def solve(H, W, A):
    min = 1000
    for i in range(H):
        for j in range(W):
            if A[i][j] < min:
                min = A[i][j]
    res = 0
    for i in range(H):
        for j in range(W):
            res += A[i][j] - min
    return res

=======
Suggestion 4

def main():
    h,w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    min = a[0][0]
    for i in range(h):
        for j in range(w):
            if min > a[i][j]:
                min = a[i][j]
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min
    print(ans)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(h)]
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
Suggestion 6

def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_A = min(map(min, A))
    print(sum(map(lambda x: sum(map(lambda y: y - min_A, x)), A)))

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    min_a = 101
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
Suggestion 8

def main():
    h,w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    min_a = min([min(row) for row in a])
    print(sum([sum([x - min_a for x in row]) for row in a]))

=======
Suggestion 9

def main():
    H,W = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(H)]
    sum_A = sum([sum(A[i]) for i in range(H)])
    min_A = min([min(A[i]) for i in range(H)])
    print(sum_A - min_A*H*W)
main()

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    min_A = min(min(A))
    count = 0
    for i in range(H):
        for j in range(W):
            count += A[i][j] - min_A
    print(count)
