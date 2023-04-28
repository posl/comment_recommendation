Synthesizing 2/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    T = []
    X = []
    A = []
    for _ in range(N):
        t, x, a = map(int, input().split())
        T.append(t)
        X.append(x)

=======
Suggestion 2

def main():
    N = int(input())
    T = [-1] * N
    X = [-1] * N
    A = [-1] * N
    for i in range(N):
        T[i], X[i],
