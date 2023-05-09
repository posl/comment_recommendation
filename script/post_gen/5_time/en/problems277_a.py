Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(n):
        if p[i] == x:
            print(i+1)
            break

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(N):
        if P[i] == X:
            print(i+1)
            break

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    print(p.index(x) + 1)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    print(P.index(X) + 1)

=======
Suggestion 5

def get_input():
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    return n, x, p

=======
Suggestion 6

def solve():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    print(P.index(X)+1)

=======
Suggestion 7

def solution():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(0, N):
        if P[i] == X:
            print(i+1)

solution()

=======
Suggestion 8

def main():
    n = int(input())
    x = int(input())
    p = [int(i) for i in input().split()]
    print(p.index(x)+1)
