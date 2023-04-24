Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > 10:
            ans += A[i] - 10
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] > 10:
            ans += a[i] - 10
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    for i in range(n):
        if a[i] > 10:
            total += a[i] - 10
    print(total)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    answer = 0
    for i in range(N):
        if A[i] > 10:
            answer += A[i] - 10
    print(answer)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in A:
        if i > 10:
            count += i - 10
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a - 10 for a in A if a > 10]
    print(sum(A))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum([ai - 10 if ai > 10 else 0 for ai in a]))
