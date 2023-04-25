Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, x, t = map(int, input().split())
    print((n + x - 1) // x * t)

=======
Suggestion 2

def main():
    N, X, T = map(int, input().split())
    print((N + X - 1) // X * T)

=======
Suggestion 3

def main():
    N, X, T = map(int, input().split())
    time = 0
    if N % X == 0:
        time = (N // X) * T
    else:
        time = (N // X + 1) * T
    print(time)

=======
Suggestion 4

def main():
    N, X, T = map(int, input().split())
    print(((N + X - 1) // X) * T)

=======
Suggestion 5

def main():
    N, X, T = map(int, input().split())
    ans = 0
    ans = N // X * T
    if N % X != 0:
        ans += T
    print(ans)
