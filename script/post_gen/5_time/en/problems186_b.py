Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min = 100
    for i in range(H):
        for j in range(W):
            if A[i][j] < min:
                min = A[i][j]
    count = 0
    for i in range(H):
        for j in range(W):
            count += A[i][j] - min
    print(count)

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    min_a = min([min(x) for x in a])
    print(sum([sum(x) for x in a]) - min_a * h * w)

=======
Suggestion 3

def main():
    H,W = map(int,input().split())
    A = []
    for i in range(H):
        A.append(list(map(int,input().split())))
    min = 100
    for i in range(H):
        for j in range(W):
            if A[i][j] < min:
                min = A[i][j]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min
    print(ans)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_a = min([min(a) for a in A])
    ans = 0
    for a in A:
        for aa in a:
            ans += aa - min_a
    print(ans)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    min_a = min([min(a[i]) for i in range(h)])
    print(sum([sum([a[i][j] - min_a for j in range(w)]) for i in range(h)]))

=======
Suggestion 6

def problem():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min = 100
    for i in range(H):
        for j in range(W):
            if A[i][j] < min:
                min = A[i][j]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min
    print(ans)

problem()

=======
Suggestion 7

def main():
    # input
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))

    # compute
    minA = 101
    for i in range(H):
        for j in range(W):
            minA = min(minA, A[i][j])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - minA

    # output
    print(ans)

=======
Suggestion 8

def solve():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    min_a = min([min(a[i]) for i in range(h)])
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a
    print(ans)

=======
Suggestion 9

def main():
    h,w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    min_a = min(min(a))
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a
    print(ans)

=======
Suggestion 10

def solve(H, W, A):
    min_num = min([min(a) for a in A])
    return sum([sum([a - min_num for a in a]) for a in A])

H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]
print(solve(H, W, A))
