Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += d[i] * d[j]
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += d[i] * d[j]
    print(sum)

=======
Suggestion 3

def main():
    n = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            sum += d[i] * d[j]
    print(sum)

=======
Suggestion 4

def main():
    N = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += d[i] * d[j]
    print(sum)

=======
Suggestion 5

def main():
    n = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            sum += d[i] * d[j]
    print(sum)

=======
Suggestion 6

def main():
    n = int(input())
    d = list(map(int, input().split()))

    ans = 0

    for i in range(0, n):
        for j in range(i+1, n):
            ans += d[i] * d[j]

    print(ans)

=======
Suggestion 7

def calc_sum_of_recovery(n, d):
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += d[i] * d[j]
    return sum
