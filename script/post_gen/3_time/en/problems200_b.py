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
            N = N // 200
        else:
            N = int(str(N) + '200')
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

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    for i in range(K):
        if N % 200 == 0:
            N //= 200
        else:
            N = int(str(N) + "200")
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
