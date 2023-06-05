Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    min_n = min(map(min, a))
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_n
    print(ans)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_A = 100
    for i in range(H):
        for j in range(W):
            if A[i][j] < min_A:
                min_A = A[i][j]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min_A
    print(ans)

=======
Suggestion 3

def problem186_b():
    pass

=======
Suggestion 4

def solve(h, w, a):
    min_a = 100
    for i in range(h):
        for j in range(w):
            min_a = min(min_a, a[i][j])

    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a

    return ans

=======
Suggestion 5

def main():
    h,w = map(int,input().split())
    a = []
    for i in range(h):
        a.append(list(map(int,input().split())))
    min_num = min(min(a))
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_num
    print(ans)

=======
Suggestion 6

def main():
    h,w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    min_a = min([min(a[i]) for i in range(h)])
    print(sum([sum(a[i]) - min_a*w for i in range(h)]))

=======
Suggestion 7

def main():
    #input
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    #process
    min_a = 100
    for i in range(h):
        for j in range(w):
            if a[i][j] < min_a:
                min_a = a[i][j]
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a
    #output
    print(ans)

=======
Suggestion 8

def solve():
    H,W = map(int,input().split())
    A = []
    for i in range(H):
        A.append(list(map(int,input().split())))
    min_a = 100
    for i in range(H):
        for j in range(W):
            min_a = min(min_a,A[i][j])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min_a
    print(ans)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min_num = min(map(min, A))
    print(sum(map(lambda x: sum(x) - min_num * W, A)))

=======
Suggestion 10

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(h)]
    min_a = 100
    for i in range(h):
        for j in range(w):
            min_a = min(min_a, a[i][j])
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a
    print(ans)
main()
