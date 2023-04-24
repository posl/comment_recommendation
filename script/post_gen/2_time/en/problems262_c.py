Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] == i + 1:
            ans += 1
    print(ans // 2)

=======
Suggestion 2

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    cnt = [0] * n
    for i in range(n):
        cnt[a[i] - 1] += 1
    ans = 0
    for i in range(n):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [0] * N

    for i in range(N):
        B[A[i] - 1] = i

    count = 0
    for i in range(N):
        if B[i] < i:
            continue
        for j in range(i + 1, N):
            if B[j] < i:
                continue
            if B[j] < B[i]:
                count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    for i in range(N):
        if A[i] == (i+1):
            result += 1
    print(result//2)

main()

I solved this problem with the following code. I think this code is not elegant, but it works.

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [1, 3, 2, 4]
    # N = 4
    # A = [5, 8, 2, 2, 1, 6, 7, 2, 9, 10]
    # N = 10
    # A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # N = 10
    # A = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    # N = 10
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # N = 10
    # A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # N = 10
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    # N = 10
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2]
    # N = 10
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3]
    # N = 10
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
    # N = 10
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
    # N = 10
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 6]
    # N = 10
    # A = [1,

=======
Suggestion 6

def solve(N, A):
    ans = 0
    for i in range(N):
        if i + 1 == A[i]:
            ans += 1
    return ans

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #a = [int(i) for i in input().split()]
    #a = [int(input()) for _ in range(n)]
    #a = [input() for _ in range(n)]
    #a = [list(map(int, input().split())) for _ in range(n)]
    #a = [list(input()) for _ in range(n)]
    #a = [input().split() for _ in range(n)]
    #a = [int(input()) for _ in range(n)]
    #a = [list(map(int, list(input()))) for _ in range(n)]
    #a = [list(input()) for _ in range(n)]
    #a = [input().split() for _ in range(n)]
    #a = [int(input()) for _ in range(n)]
    #a = [list(map(int, list(input()))) for _ in range(n)]
    #a = [list(input()) for _ in range(n)]
    #a = [input().split() for _ in range(n)]
    #a = [int(input()) for _ in range(n)]
    #a = [list(map(int, list(input()))) for _ in range(n)]
    #a = [list(input()) for _ in range(n)]
    #a = [input().split() for _ in range(n)]
    #a = [int(input()) for _ in range(n)]
    #a = [list(map(int, list(input()))) for _ in range(n)]
    #a = [list(input()) for _ in range(n)]
    #a = [input().split() for _ in range(n)]
    #a = [int(input()) for _ in range(n)]
    #a = [list(map(int, list(input()))) for _ in range(n)]
    #a = [list(input()) for _ in range(n)]
    #a = [input().split() for _ in range(n)]
    #a = [int(input()) for _ in range(n)]
    #a = [list(map(int, list(input()))) for _ in range(n)]
    #a = [list(input()) for _ in range(n)]
    #a = [input().split() for _ in range(n)]
    #a = [int(input()) for _ in range(n)]
    #a = [list(map(int, list(input

=======
Suggestion 8

def main():
    N = int(input())
    a = list(map(int, input().split()))
    #print(N)
    #print(a)

    #aの値がiのとき、aの値がiである要素のindexをa[i]に格納する
    a_index = [0] * (N+1)
    for i in range(N):
        a_index[a[i]] = i+1

    #print(a_index)

    #aの値がiのとき、aの値がiである要素のindexのうち、最小のものをa_min[i]に格納する
    a_min = [0] * (N+1)
    for i in range(1, N+1):
        if i == 1:
            a_min[i] = a_index[i]
        else:
            a_min[i] = min(a_min[i-1], a_index[i])

    #print(a_min)

    #aの値がiのとき、aの値がiである要素のindexのうち、最大のものをa_max[i]に格納する
    a_max = [0] * (N+1)
    for i in range(N, 0, -1):
        if i == N:
            a_max[i] = a_index[i]
        else:
            a_max[i] = max(a_max[i+1], a_index[i])

    #print(a_max)

    #a_min[i] <= a_max[i]のとき、(a_min[i], a_max[i])は条件を満たす
    ans = 0
    for i in range(1, N+1):
        if a_min[i] <= a_max[i]:
            ans += 1

    print(ans)
