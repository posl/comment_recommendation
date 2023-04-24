Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        if a > 10:
            ans += a - 10
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        if A[i] > 10:
            sum += A[i] - 10
    print(sum)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        if A[i] > 10:
            ans += A[i] - 10
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    for i in range(n):
        if a[i] > 10:
            total += a[i] - 10
    print(total)

main()

=======
Suggestion 5

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] > 10:
            ans += a[i] - 10
    print(ans)

solve()

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum([max(0, a - 10) for a in A]))

=======
Suggestion 7

def main():
    n = int(input())
    a = map(int, input().split())
    print(sum(max(0, x - 10) for x in a))

=======
Suggestion 8

def get_input():
    N = int(input())
    A = [int(a) for a in input().split()]
    return N, A
