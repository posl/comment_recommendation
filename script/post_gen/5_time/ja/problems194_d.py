Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(1,n):
        ans += n/(n-i)
    print(ans)
main()

=======
Suggestion 2

def main():
    N = int(input())
    print(N + N * (N - 1) / 2)

=======
Suggestion 3

def main():
    n = int(input())
    print((n-1)*2/n)

=======
Suggestion 4

def main():
    n = int(input())
    print((n-1) * (1 + 1/(n-1)))

=======
Suggestion 5

def main():
    N = int(input())
    print((N-1)*2/(N*(N-1)))

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1,N):
        ans += (1/N)/(1-(1/N)) * i
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    print((N-1)*2)

=======
Suggestion 8

def main():
    n = int(input())
    print((n-1)*2/n+1)

=======
Suggestion 9

def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        ans += n / i
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    print((N * (N+1) / 2) / (N-1))
