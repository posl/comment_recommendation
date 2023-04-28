Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k * d:
        print(x - k * d)
    else:
        m = x // d
        if (k - m) % 2 == 0:
            print(x - m * d)
        else:
            print(d - x + m * d)

=======
Suggestion 2

def main():
    # input
    X, K, D = map(int, input().split())

    # compute

    # output
    print()

=======
Suggestion 3

def problems175_c():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x - k * d > 0:
        print(x - k * d)
    else:
        if (k - x // d) % 2 == 0:
            print(x % d)
        else:
            print(d - x % d)

=======
Suggestion 4

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k*d:
        print(x - k*d)
    else:
        if (k*d - x) % (2*d) == 0:
            print(0)
        else:
            print(abs((k*d - x) % (2*d) - d))

=======
Suggestion 5

def problem175_c():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k * d:
        print(x - k * d)
    else:
        if (k - x // d) % 2 == 0:
            print(x % d)
        else:
            print(d - x % d)

=======
Suggestion 6

def solve(x, k, d):
    if x < 0:
        x = -x
    if x // d >= k:
        return x - k * d
    elif (k - x // d) % 2 == 0:
        return x - (x // d) * d
    else:
        return d - x + (x // d) * d

=======
Suggestion 7

def problems175_c():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k*d:
        print(x - k*d)
    else:
        if (k*d - x) % (2*d) == 0:
            print(0)
        else:
            print(min(abs(x - (k*d - x) % (2*d)), abs(x - (k*d - x) % (2*d) - 2*d)))

=======
Suggestion 8

def main():
    X, K, D = map(int, input().split())
    if X < 0:
        X = -X
    if X//D >= K:
        print(X-K*D)
        return
    K -= X//D
    X %= D
    if K%2 == 0:
        print(X)
    else:
        print(D-X)

=======
Suggestion 9

def problems175_c():
    x,k,d = map(int, input().split())
    x = abs(x)
    if x//d > k:
        print(x-k*d)
    else:
        if (x//d)%2 == k%2:
            print(x%d)
        else:
            print(d-x%d)

=======
Suggestion 10

def problems175_c(x, k, d):
    if x < 0:
        x = -x
    if x//d >= k:
        return x - k*d
    else:
        x = x%d
        k -= x//d
        if k%2 == 0:
            return x
        else:
            return d-x
