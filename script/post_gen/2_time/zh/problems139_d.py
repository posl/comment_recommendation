Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    print(int(n*(n-1)/2))

=======
Suggestion 2

def main():
    n = int(input())
    if n == 1:
        print(0)
    else:
        print(n*(n-1))

=======
Suggestion 3

def solve(n):
    ans = 0
    for i in range(1, n + 1):
        ans += i % (n + 1)
    return ans

n = int(input())
print(solve(n))

=======
Suggestion 4

def main():
    N = int(input())
    if N == 1:
        print(0)
    elif N == 2:
        print(1)
    else:
        print((N-1)*(N-2)//2)

=======
Suggestion 5

def get_max_M(N):
    if N == 1:
        return 0
    if N == 2:
        return 1
    if N % 2 == 0:
        return int(N / 2) * int(N / 2)
    else:
        return int(N / 2) * int(N / 2 + 1)

=======
Suggestion 6

def main():
    n = int(input())
    answer = 0
    for i in range(1, n+1):
        answer += i - 1
    print(answer)

=======
Suggestion 7

def main():
    N = int(input())
    i = 1
    sum = 0
    while i <= N:
        sum += N % i
        i += 1
    print(sum)

=======
Suggestion 8

def solve(n):
    if n==1:
        return 0
    else:
        return n*(n-1)//2

=======
Suggestion 9

def problem139_d():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        ans += i
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    if N == 1:
        print(0)
    else:
        print(N*(N-1)//2)

main()
