Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    ans = 0
    for i in range(1, N):
        ans += (N - 1) // i
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    if N == 1:
        print(0)
    else:
        print(N*(N-1)//2)

=======
Suggestion 3

def main():
    N = int(input())
    if N == 1:
        print(0)
    elif N == 2:
        print(1)
    else:
        print(N + N - 2)

=======
Suggestion 4

def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    print(N * (N - 1) // 2)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += (N-1)//i
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    if n == 1:
        print(0)
    else:
        print(n * (n-1) // 2)

=======
Suggestion 7

def main():
    N = int(input())
    if N == 1:
        print(0)
    else:
        print(N + (N-2)*(N-1)//2)

main()

=======
Suggestion 8

def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    # M_1 + M_2 + ... + M_N = (N-1) + (N-2) + ... + 1 = N*(N-1)/2
    print(N*(N-1)//2)

=======
Suggestion 9

def main():
    N = int(input())
    print(N*(N-1)//2)

main()

=======
Suggestion 10

def main():
    n = int(input())
    print((n - 1) * n // 2)
