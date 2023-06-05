Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    satisfaction = 0
    for i in range(n):
        satisfaction += b[a[i]-1]
        if i < n-1 and a[i+1] == a[i] + 1:
            satisfaction += c[a[i]-1]
    print(satisfaction)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    score = 0
    for i in range(n):
        score += b[a[i]-1]
        if i < n-1 and a[i+1] == a[i]+1:
            score += c[a[i]-1]

    print(score)


main()

=======
Suggestion 3

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    score = 0
    for i in range(N):
        score += B[A[i]-1]
        if i < N-1 and A[i] == A[i+1] - 1:
            score += C[A[i]-1]
    print(score)

=======
Suggestion 4

def get_satisfaction_score(N, A, B, C):
    score = 0
    for i in range(N):
        score += B[A[i]-1]
        if i != N-1 and A[i] + 1 == A[i+1]:
            score += C[A[i]-1]
    return score

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    sum = 0
    for i in range(n):
        sum += b[a[i]-1]
        if i > 0 and a[i] - a[i-1] == 1:
            sum += c[a[i-1]-1]
    print(sum)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    result = 0
    for i in range(n):
        result += b[a[i] - 1]
        if i < n - 1 and a[i + 1] == a[i] + 1:
            result += c[a[i] - 1]

    print(result)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    satisfaction = 0
    for i in range(N):
        satisfaction += B[A[i] - 1]
        if i != N - 1 and A[i] + 1 == A[i + 1]:
            satisfaction += C[A[i] - 1]
    print(satisfaction)

=======
Suggestion 8

def main():
    #读取数据
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]

    #计算满意度积分
    score = 0
    score += B[A[0]-1]
    for i in range(1, N):
        score += B[A[i]-1]
        if A[i] == A[i-1] + 1:
            score += C[A[i-1]-1]
    print(score)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    score = 0
    for i in range(n):
        score += b[a[i]-1]
        if i < n-1 and a[i]+1 == a[i+1]:
            score += c[a[i]-1]

    print(score)

=======
Suggestion 10

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    score = 0
    for i in range(n):
        score += b[a[i]-1]
        if i < n-1 and a[i]+1 == a[i+1]:
            score += c[a[i]-1]
    print(score)
