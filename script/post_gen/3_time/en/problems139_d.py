Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N == 1:
        print(0)
    else:
        print(N * (N - 1) // 2)

=======
Suggestion 2

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
Suggestion 3

def main():
    N = int(input())
    if N == 1:
        print(0)
    elif N == 2:
        print(1)
    else:
        print(N - 2)

=======
Suggestion 4

def main():
    n = int(input())
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    else:
        print(n*(n-1)//2)

=======
Suggestion 5

def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    print(N * (N - 1) // 2)

=======
Suggestion 6

def main():
    N = int(input())
    if N % 2 == 0:
        print(int((N/2)*(N-1)))
    else:
        print(int((N/2)*(N-1)+N/2))

=======
Suggestion 7

def main():
    n = int(input())
    print(n * (n - 1) // 2)

=======
Suggestion 8

def main():
    N = int(input())
    ans = (N-1)*N//2
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    print((N-1)*N//2)
