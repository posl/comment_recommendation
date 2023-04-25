Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, X, T, D = map(int, input().split())
    if M >= X:
        print(T + (N - M) * D)
    else:
        print(T + (X - M) * D + (N - X) * D)

=======
Suggestion 2

def main():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        print(T + (N - M) * D)
    else:
        print(T + (N - X) * D)

=======
Suggestion 3

def main():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        print(T + (N - M) * D)
    else:
        print(T - (M - X) * D)
main()

=======
Suggestion 4

def main():
    n, m, x, t, d = map(int, input().split())
    if m < x:
        print(t + (n - x) * d)
    else:
        print(t - (x - m) * d)

=======
Suggestion 5

def main():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        print(T + D * (N - X))
    else:
        print(T + D * (N - M - 1))

=======
Suggestion 6

def main():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        height = T + (M * D)
    else:
        height = T + ((X - 1) * D)
    print(height)

=======
Suggestion 7

def main():
    n, m, x, t, d = [int(i) for i in input().split()]
    print(t + d * (m - x) if m < x else t + d * (n - x))

=======
Suggestion 8

def main():
    #input
    N, M, X, T, D = map(int, input().split())

    #compute
    if M < X:
        ans = T + (N-M) * D
    else:
        ans = T + (N-X) * D

    #output
    print(ans)

=======
Suggestion 9

def main():
    N, M, X, T, D = map(int, input().split())
    print(T + (M - X) * D if M > X else T)

=======
Suggestion 10

def takahashiHeight(N, M, X, T, D):
    if (M < X):
        return T + (M * D)
    else:
        return T + (X * D) + ((M - X) * D)
