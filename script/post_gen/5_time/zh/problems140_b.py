Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def get_score(n, dish, satisfaction, bonus):
    score = 0
    for i in range(n):
        score += satisfaction[dish[i]-1]
        if i < n-1 and dish[i] == dish[i+1]-1:
            score += bonus[dish[i]-1]
    return score

=======
Suggestion 3

def main():
    # N = 3
    # A = [3, 1, 2]
    # B = [2, 5, 4]
    # C = [3, 6]
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    satisfaction = 0
    for i in range(N):
        satisfaction += B[A[i] - 1]
        if i < N - 1 and A[i + 1] - A[i] == 1:
            satisfaction += C[A[i] - 1]

    print(satisfaction)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    sum = 0
    for i in range(n):
        sum += b[a[i] - 1]
        if i < n - 1 and a[i] + 1 == a[i + 1]:
            sum += c[a[i] - 1]
    print(sum)

=======
Suggestion 5

def get_satisfaction(n, a, b, c):
    satisfaction = 0
    for i in range(n):
        satisfaction += b[a[i]-1]
        if i < n-1 and a[i+1] == a[i]+1:
            satisfaction += c[a[i]-1]
    return satisfaction

=======
Suggestion 6

def sum_score(a,b,c):
    score = 0
    for i in range(len(a)):
        score += b[a[i]-1]
        if i < len(a)-1:
            if a[i+1] == a[i] + 1:
                score += c[a[i]-1]
    return score

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = b[a[0] - 1]
    for i in range(n - 1):
        ans += b[a[i + 1] - 1]
        if a[i] + 1 == a[i + 1]:
            ans += c[a[i] - 1]

    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    satisfaction = 0
    for i in range(n):
        satisfaction += b[a[i]-1]
        if i < n-1:
            if a[i]+1 == a[i+1]:
                satisfaction += c[a[i]-1]
    print(satisfaction)

=======
Suggestion 9

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]

    score = 0
    for i in range(n):
        score += b[a[i]-1]
        if i != n -1 and a[i] + 1 == a[i+1]:
            score += c[a[i]-1]
    print(score)
