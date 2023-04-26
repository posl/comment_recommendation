Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += B[A[i]-1]
        if i > 0 and A[i] == A[i-1] + 1:
            ans += C[A[i-1]-1]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += B[A[i]-1]
        if i > 0 and A[i] - A[i-1] == 1:
            ans += C[A[i-1]-1]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += B[A[i]-1]
        if i != N-1 and A[i] == A[i+1]-1:
            ans += C[A[i]-1]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += B[A[i]-1]
        if i != N-1 and A[i+1] == A[i]+1:
            ans += C[A[i]-1]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        ans += B[A[i] - 1]
        if i != 0 and A[i] - A[i - 1] == 1:
            ans += C[A[i - 1] - 1]

    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]

    ans = 0
    for i in range(N):
        ans += B[A[i] - 1]
        if i != N - 1 and A[i] + 1 == A[i + 1]:
            ans += C[A[i] - 1]

    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        ans += b[a[i]-1]
        if i > 0 and a[i] - a[i-1] == 1:
            ans += c[a[i-1]-1]
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    point = 0
    for i in range(N):
        point += B[A[i]-1]
        if i != N-1 and A[i] == A[i+1]-1:
            point += C[A[i]-1]
    print(point)

=======
Suggestion 9

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    #解答
    ans = 0
    for i in range(N):
        ans += B[A[i]-1]
        if i != N-1:
            if A[i] == A[i+1]-1:
                ans += C[A[i]-1]
    #出力
    print(ans)
