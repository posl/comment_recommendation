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
main()

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] > 10:
            count += A[i] - 10
    print(count)

=======
Suggestion 4

def calc(x):
    if x < 10:
        return 0
    else:
        return x - 10

n = int(input())
a = list(map(int,input().split()))

print(sum(map(calc,a)))

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    ans = 0
    for i in range(N):
        if A[i] > 10:
            ans += A[i] - 10
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in a:
        if i > 10:
            ans += i - 10
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    answer = 0
    for a in A:
        if a > 10:
            answer += a - 10
    print(answer)

=======
Suggestion 8

def f(n):
    if n < 10:
        return 0
    else:
        return n - 10

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] > 10:
            ans += a[i] - 10
    print(ans)
