Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if X // D >= K:
        print(X - K * D)
    else:
        if (K - X // D) % 2 == 0:
            print(X % D)
        else:
            print(abs(X % D - D))

=======
Suggestion 2

def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if X >= K * D:
        print(X - K * D)
    else:
        if (K - X // D) % 2 == 0:
            print(X % D)
        else:
            print(abs(X % D - D))

=======
Suggestion 3

def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if K * D <= X:
        print(X - K * D)
    else:
        K -= X // D
        X %= D
        if K % 2 == 0:
            print(X)
        else:
            print(D - X)

=======
Suggestion 4

def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if K * D <= X:
        print(X - K * D)
    else:
        K -= X // D
        X %= D
        if K % 2 == 0:
            print(X)
        else:
            print(abs(X - D))

=======
Suggestion 5

def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    m = min(X // D, K)
    X -= m * D
    K -= m
    if K % 2 == 0:
        print(X)
    else:
        print(abs(X - D))

=======
Suggestion 6

def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if X - K * D >= 0:
        print(X - K * D)
    else:
        if (K - X // D) % 2 == 0:
            print(X % D)
        else:
            print(abs(X % D - D))

=======
Suggestion 7

def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if X // D > K:
        print(X - K * D)
        return
    if (K - X // D) % 2 == 0:
        print(X % D)
    else:
        print(abs(X % D - D))

=======
Suggestion 8

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k * d:
        print(x - k * d)
        return
    else:
        if (k - x // d) % 2 == 0:
            print(abs(x - (x // d) * d))
        else:
            print(abs(x - (x // d + 1) * d))

=======
Suggestion 9

def main():
    x,k,d = map(int,input().split())
    if x < 0:
        x = -x
    if k <= x // d:
        print(x - k * d)
    else:
        if (k - x // d) % 2 == 0:
            print(x % d)
        else:
            print(abs((x % d) - d))

=======
Suggestion 10

def main():
    x, k, d = map(int, input().split())
    #print(x, k, d)
    x = abs(x)
    #print(x)
    if x > k * d:
        print(x - k * d)
    else:
        k -= x // d
        x %= d
        if k % 2 == 0:
            print(x)
        else:
            print(d - x)
