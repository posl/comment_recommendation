Synthesizing 10/10 solutions

=======
Suggestion 1

def get_score(A, B, C):
    score = 0
    for i in range(len(A)):
        score += B[A[i]-1]
        if i < len(A)-1:
            if A[i+1] == A[i] + 1:
                score += C[A[i]-1]
    return score

=======
Suggestion 2

def cal_satisfaction():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    satisfaction = 0
    for i in range(n):
        satisfaction += b[a[i]-1]
        if i < n-1 and a[i]+1 == a[i+1]:
            satisfaction += c[a[i]-1]
    print(satisfaction)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    total = 0
    for i in range(N):
        total += B[A[i]-1]
        if i != N-1 and A[i] == A[i+1] - 1:
            total += C[A[i]-1]
    print(total)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    score = 0
    for i in range(n):
        score += b[a[i]-1]
        if i < n-1 and a[i+1] == a[i] + 1:
            score += c[a[i]-1]
    print(score)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    satisfaction = 0
    prev = a[0]
    satisfaction += b[prev-1]
    for i in range(1, n):
        current = a[i]
        satisfaction += b[current-1]
        if prev + 1 == current:
            satisfaction += c[prev-1]
        prev = current
    print(satisfaction)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    sum = 0
    for i in range(n):
        sum += b[a[i]-1]
        if i < n-1 and a[i] == a[i+1]-1:
            sum += c[a[i]-1]
    print(sum)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    sum = 0
    for i in range(N):
        sum += B[A[i] - 1]
        if i < N - 1 and A[i] + 1 == A[i + 1]:
            sum += C[A[i] - 1]

    print(sum)

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    total = 0
    for i in range(N):
        total += B[A[i]-1]
        if i < N-1 and A[i+1] == A[i]+1:
            total += C[A[i]-1]
    print(total)

main()

=======
Suggestion 9

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    total = 0
    for i in range(n):
        total += b[a[i]-1]
        if i < n - 1 and a[i+1] - a[i] == 1:
            total += c[a[i]-1]
    print(total)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    sum = 0
    for i in range(n):
        sum += b[a[i]-1]
        if i != n-1 and a[i] == a[i+1]-1:
            sum += c[a[i]-1]
    print(sum)
