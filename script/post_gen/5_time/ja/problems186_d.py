Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (2 * i - n + 1)
    print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (2*i - N + 1)
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort()
    ans = 0
    for i in range(n):
        ans += a_list[i] * (n - i - 1) - a_list[i] * i
    print(ans * 2)

=======
Suggestion 4

def solver():
    N = int(input())
    A = sorted(list(map(int,input().split())))
    #print(A)
    ans = 0
    for i in range(1,N):
        ans += A[i] - A[i-1]
        #print(ans)
    ans *= 2
    ans += A[N-1] - A[0]
    print(ans)
    return 0

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (i) - A[i] * (N - i - 1)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (2*i-N+1)
    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    # N = 3
    # A = [5, 1, 2]
    # N = 5
    # A = [31, 41, 59, 26, 53]

    A.sort()
    # print(A)
    # print(A[N-1] - A[0])
    # print(A[N-2] - A[0])
    # print(A[N-1] - A[1])
    # print(A[N-2] - A[1])
    # print(A[N-1] - A[2])
    # print(A[N-2] - A[2])
    # print(A[N-3] - A[0])
    # print(A[N-3] - A[1])
    # print(A[N-3] - A[2])
    # print(A[N-3] - A[3])
    # print(A[N-4] - A[0])
    # print(A[N-4] - A[1])
    # print(A[N-4] - A[2])
    # print(A[N-4] - A[3])
    # print(A[N-4] - A[4])

    # print(A[N-1] - A[0])
    # print(A[N-2] - A[0])
    # print(A[N-3] - A[0])
    # print(A[N-4] - A[0])
    # print(A[N-5] - A[0])
    # print(A[N-1] - A[1])
    # print(A[N-2] - A[1])
    # print(A[N-3] - A[1])
    # print(A[N-4] - A[1])
    # print(A[N-5] - A[1])
    # print(A[N-1] - A[2])
    # print(A[N-2] - A[2])
    # print(A[N-3] - A[2])
    # print(A[N-4] - A[2])
    # print(A[N-5] - A[2])
    # print(A[N-1] - A[3])
    # print(A[N-2] - A[3])
    # print(A[N-3] - A

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(1, N):
        sum += A[i] * i - A[i-1] * (N - i)
    print(sum)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(1, N):
        sum += A[i] - A[i-1]
    print(sum * 2)

=======
Suggestion 10

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort()
    ans = 0
    for i in range(n):
        ans += a_list[i] * (i + 1)
    ans -= sum(a_list)
    ans *= 2
    print(ans)
