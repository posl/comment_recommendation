Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    tmp = 0
    for i in range(N):
        tmp += A[i]
        ans = max(ans, tmp)
        if tmp < 0:
            tmp = 0

    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    max = 0
    for i in range(N):
        max += A[i]
        if max < 0:
            max = 0
    print(max)

main()

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int,input().split()))
    max = 0
    for i in range(N):
        max += A[i]
        if max < 0:
            max = 0
    print(max)

=======
Suggestion 4

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #N = 5
    #A = [-2, 1, 3, -1, -1]
    #N = 5
    #A = [-1000, -1000, -1000, -1000, -1000]
    #N = 3
    #A = [2, -1, -2]
    #N = 3
    #A = [2, 1, 2]
    #N = 3
    #A = [-2, -1, -2]
    #N = 3
    #A = [-2, 1, 2]
    #N = 3
    #A = [2, -1, 2]
    #N = 3
    #A = [-2, 1, -2]
    #N = 3
    #A = [2, -1, -2]
    #N = 3
    #A = [2, 1, -2]
    #N = 3
    #A = [-2, -1, 2]
    #N = 3
    #A = [-2, 1, -2]
    #N = 3
    #A = [-2, 1, 2]

    #処理
    #min_ = 0
    #max_ = 0
    #for i in range(N):
    #    if i % 2 == 0:
    #        min_ += A[i]
    #        max_ += A[i]
    #    else:
    #        min_ -= A[i]
    #        max_ -= A[i]
    #    if min_ > max_:
    #        min_, max_ = max_, min_
    #print(max_)

    #処理
    #min_ = 0
    #max_ = 0
    #for i in range(N):
    #    if i % 2 == 0:
    #        min_ += A[i]
    #        max_ += A[i]
    #    else:
    #        min_ -= A[i]
    #        max_ -= A[i]
    #    if min

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0]
    for i in range(N):
        B.append(B[i]+A[i])
    print(max(B)-min(B))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += max(a[i], 0)
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += abs(A[i])
    ans -= max(A)
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    A = [A[i] + A[i - 1] for i in range(1, N + 1)]
    print(max(A) - min(A))

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(A)
    A.sort(reverse=True)
    #print(A)
    #print(sum(A))
    if sum(A) <= 0:
        print(0)
    else:
        print(sum(A[:N-1]))
