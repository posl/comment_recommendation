Synthesizing 10/10 solutions

=======
Suggestion 1

def problems140_b():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    score = 0
    for i in range(N):
        score += B[A[i]-1]
        if i < N-1 and A[i+1]-A[i] == 1:
            score += C[A[i]-1]
    print(score)

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    S = 0
    for i in range(N):
        S += B[A[i]-1]
        if i < N-1 and A[i+1] - A[i] == 1:
            S += C[A[i]-1]
    print(S)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    #print(N)
    #print(A)
    #print(B)
    #print(C)

    score = 0
    for i in range(N):
        score += B[A[i]-1]
        if i < N-1 and A[i]+1 == A[i+1]:
            score += C[A[i]-1]
    print(score)

=======
Suggestion 4

def get_max_score(N, A, B, C):
    max_score = 0
    for i in range(N):
        score = 0
        score += B[A[i]-1]
        if i < N-1:
            score += C[A[i]-1]
        if score > max_score:
            max_score = score
    return max_score

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
        if i != n-1:
            if a[i+1] - a[i] == 1:
                sum += c[a[i]-1]
    print(sum)

=======
Suggestion 6

def main():
    total = 0
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    for i in range(N):
        total += B[A[i]-1]
        if i < N-1 and A[i+1] == A[i] + 1:
            total += C[A[i]-1]

    print(total)

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]

    sum = 0
    for i in range(n):
        sum += b[a[i] - 1]
        if i > 0 and a[i] == a[i - 1] + 1:
            sum += c[a[i - 1] - 1]

    print(sum)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    total = 0
    for i in range(n):
        total += b[a[i]-1]
        if i < n-1 and a[i+1] == a[i]+1:
            total += c[a[i]-1]

    print(total)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans += b[a[i]-1]
        if i > 0 and a[i] == a[i-1] + 1:
            ans += c[a[i-1]-1]
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    score = 0
    for i in range(n):
        score += b[a[i] - 1]
        if i > 0 and a[i] - a[i - 1] == 1:
            score += c[a[i - 1] - 1]
    print(score)
