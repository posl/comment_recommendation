Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'U':
            X = X // 2
        elif S[i] == 'L':
            X = 2 * X - 1
        else:
            X = 2 * X + 1
    print(X)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'U':
            X = (X + 1) // 2
        elif S[i] == 'L':
            X *= 2
        elif S[i] == 'R':
            X = X * 2 + 1
    print(X)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == "U":
            if X % 2 == 1:
                X = (X - 1) // 2
        elif S[i] == "L":
            X = X * 2 + 1
        elif S[i] == "R":
            X = X * 2
    print(X)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == "U":
            X = (X - 1) // 2
        elif S[i] == "L":
            X = X * 2
        else:
            X = X * 2 + 1
    print(X)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'U':
            if X % 2 == 0:
                X = X // 2
        elif S[i] == 'L':
            X = 2 * X - 1
        elif S[i] == 'R':
            X = 2 * X + 1
    print(X)

=======
Suggestion 6

def main():
    N,X = map(int,input().split())
    S = input()
    for i in range(N):
        if S[i] == 'U':
            X = X//2
        elif S[i] == 'L':
            X = (X-1)//2
        else:
            X = (X+1)//2
    print(X)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == 'U':
            X = (X - 1) // 2
        elif s == 'L':
            X = 2 * X - 1
        else:
            X = 2 * X + 1
    print(X)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == "U":
            if X % 2 == 0:
                X //= 2
        elif s == "L":
            X *= 2
        elif s == "R":
            X = X * 2 + 1
    print(X)

=======
Suggestion 9

def main():
    N,X = map(int,input().split())
    S = input()
    for s in S:
        if s == 'U':
            X = (X-1)//2
        elif s == 'L':
            X = 2*X
        else:
            X = 2*X+1
    print(X)

=======
Suggestion 10

def main():
    import sys
    input = sys.stdin.readline
    N, X = map(int, input().split())
    S = input().rstrip()
    # X が 10^18 以下なので、2^100 以下の完全二分木を考えればよい
    # これは 2^100-1 以下の完全二分木で、これは 2^99-1 以下の完全二分木で、…
    # これは 2^1-1 以下の完全二分木で、これは 1 以下の完全二分木である
    # つまり、完全二分木の頂点数は 2^k-1 である
    # ここで、k は 1 以上 100 以下の整数である
    # したがって、完全二分木の高さは 100 以下である
    # したがって、N は 100 以下である
    # したがって、S は 100 文字以下である
    # したがって、N^2 以下の計算量で解ける
    ans = X
    for i in range(N):
        if S[i] == "U":
            ans = ans // 2
        elif S[i] == "L":
            ans = ans * 2 - 1
        else:
            ans = ans * 2
    print(ans)
