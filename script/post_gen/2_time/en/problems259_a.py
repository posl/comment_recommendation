Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        print(T + (N - X) * D)
    else:
        print(T - (M - X) * D)

=======
Suggestion 2

def main():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        print(T + D * (N - X))
    else:
        print(T + D * (N - X) - D * (M - X))

=======
Suggestion 3

def main():
    N, M, X, T, D = map(int, input().split())
    if N == M:
        print(T)
    elif N == X:
        print(T + (N - M) * D)
    else:
        print(T + (X - M) * D)

=======
Suggestion 4

def main():
    n, m, x, t, d = map(int, input().split())
    if n == m:
        print(t)
    elif m < x:
        print(t + (x - m) * d)
    else:
        print(t + (n - m) * d)

=======
Suggestion 5

def main():
    N, M, X, T, D = map(int, input().split())
    #print(N, M, X, T, D)
    if M < X:
        print(T + D * (N - X))
    else:
        print(T + D * (N - M - 1))

=======
Suggestion 6

def main():
    #input
    N, M, X, T, D = map(int, input().split())

    #compute
    if M < X:
        ans = T + (N - X) * D
    else:
        ans = T + (M - X) * D + (N - M) * D

    #output
    print(ans)

=======
Suggestion 7

def solution():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        print(T + D * (N - X))
    else:
        print(T + D * (M - X))

=======
Suggestion 8

def main():
    N, M, X, T, D = map(int, input().split())
    result = T
    if M < X:
        result += (X - M) * D
    elif M > X:
        result += (N - M) * D
    print(result)

=======
Suggestion 9

def main():
    #input
    N, M, X, T, D = map(int, input().split())

    #compute
    if M >= X:
        h = T + D*(M-X)
    else:
        h = T

    #output
    print(h)

=======
Suggestion 10

def main():
    #Read the input
    N, M, X, T, D = map(int, input().split())
    #Calculate the height
    if M < X:
        height = T + (X - M) * D
    else:
        height = T
    #Print the answer
    print(height)
