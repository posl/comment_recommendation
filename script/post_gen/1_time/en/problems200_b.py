Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    for i in range(K):
        if N % 200 == 0:
            N = N // 200
        else:
            N = int(str(N) + "200")
    print(N)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    for i in range(K):
        if N % 200 == 0:
            N //= 200
        else:
            N = int(str(N) + "200")
    print(N)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    for _ in range(K):
        if N % 200 == 0:
            N //= 200
        else:
            N = int(str(N) + '200')
    print(N)
main()

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    for _ in range(K):
        if N % 200 == 0:
            N //= 200
        else:
            N = int(str(N) + '200')
    print(N)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    for i in range(K):
        if N % 200 == 0:
            N //= 200
        else:
            N = int(str(N) + '200')
    print(N)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    for _ in range(k):
        if n % 200 == 0:
            n //= 200
        else:
            n = int(str(n) + "200")
    print(n)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())

    for i in range(K):
        if N % 200 == 0:
            N //= 200
        else:
            N = int(str(N) + "200")

    print(N)

main()

Last modified: 2021-03-15 19:00:31 +0900
