Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k * d:
        print(x - k * d)
    else:
        k -= x // d
        x %= d
        if k % 2 == 0:
            print(x)
        else:
            print(d - x)

=======
Suggestion 2

def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if X // D >= K:
        print(X - D * K)
    else:
        if (K - X // D) % 2 == 0:
            print(X - X // D * D)
        else:
            print(X - (X // D + 1) * D)
main()

=======
Suggestion 3

def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if X // D >= K:
        print(X - D * K)
    else:
        if (K - X // D) % 2 == 0:
            print(X % D)
        else:
            print(abs(X % D - D))

=======
Suggestion 4

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    m = x // d
    if m >= k:
        print(x - k * d)
    else:
        if (k - m) % 2 == 0:
            print(x - m * d)
        else:
            print(abs(x - (m + 1) * d))

=======
Suggestion 5

def main():
    x, k, d = map(int, input().split())
    if x < 0:
        x = -x
    if x // d >= k:
        print(x - k * d)
    else:
        if (k - x // d) % 2 == 0:
            print(x % d)
        else:
            print(d - x % d)

=======
Suggestion 6

def main():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x//d >= k:
        print(x-d*k)
    else:
        if (k-x//d)%2 == 0:
            print(x%d)
        else:
            print(abs(x%d-d))

=======
Suggestion 7

def main():
    X,K,D = map(int,input().split())
    X = abs(X)
    if X//D > K:
        print(X-D*K)
    else:
        if (K-X//D)%2 == 0:
            print(X%D)
        else:
            print(abs(X%D-D))

=======
Suggestion 8

def main():
    X, K, D = map(int, input().split())

    X = abs(X)
    if X > K * D:
        print(X - K * D)
        return

    K -= X // D
    X %= D
    if K % 2 == 0:
        print(X)
    else:
        print(abs(X - D))

=======
Suggestion 9

def main():
    # input
    X, K, D = map(int, input().split())

    # compute
    X = abs(X)
    if X <= K*D:
        K -= X//D
        X %= D
        if K%2 == 1:
            X = abs(X-D)

    # output
    print(X)
