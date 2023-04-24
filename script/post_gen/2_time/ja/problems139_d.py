Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N % 2 == 0:
        print(N * (N - 1) // 2)
    else:
        print(N * (N - 1) // 2 + 1)

=======
Suggestion 2

def main():
    N = int(input())
    if N == 1:
        print(0)
    elif N == 2:
        print(1)
    else:
        print(N * (N - 1) // 2)
main()

=======
Suggestion 3

def main():
    N = int(input())
    if N == 1:
        print(0)
        exit()
    elif N % 2 == 0:
        print(N // 2 - 1)
    else:
        print(N // 2)

=======
Suggestion 4

def main():
    N = int(input())
    print(N * (N - 1) // 2)

=======
Suggestion 5

def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    print(n * (n - 1) // 2)

=======
Suggestion 6

def main():
    n = int(input())
    if n == 1:
        print(0)
    else:
        print((n - 1) * (n // 2) + n % 2)

main()

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        ans += (N//i) * (i-1)
        ans += max(0, N%i - i//2)
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    print((N - 1) * N // 2)

=======
Suggestion 9

def main():
    N = int(input())
    M = 0
    for i in range(1,N+1):
        M += (N//i) * (i-1) * (N//i)
        if N%i != 0:
            M += (N%i) * (N//i)
    print(M)
