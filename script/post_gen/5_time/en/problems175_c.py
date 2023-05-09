Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if X // D >= K:
        print(X - K * D)
    else:
        K -= X // D
        X %= D
        if K % 2 == 0:
            print(X)
        else:
            print(D - X)

=======
Suggestion 2

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x - d * k >= 0:
        print(x - d * k)
    else:
        if (x // d) % 2 == k % 2:
            print(x % d)
        else:
            print(abs(x % d - d))

=======
Suggestion 3

def main():
    # Take input Here and Call solution function
    x, k, d = get_ints_in_variables()
    print(solution(x, k, d))

=======
Suggestion 4

def solve(x, k, d):
    x = abs(x)
    if x > k * d:
        return x - k * d
    else:
        k -= x // d
        x %= d
        if k % 2 == 0:
            return x
        else:
            return d - x

=======
Suggestion 5

def solve():
    #import sys
    #input = sys.stdin.readline
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= d * k:
        print(x - d * k)
    else:
        k -= x // d
        x %= d
        if k % 2 == 0:
            print(x)
        else:
            print(d - x)

=======
Suggestion 6

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k * d:
        print(x - k * d)
        return
    q = x // d
    if (k - q) % 2 == 0:
        print(x - q * d)
    else:
        print(d - x + q * d)

=======
Suggestion 7

def main():
    # input
    X, K, D = map(int, input().split())
    # compute
    X = abs(X)
    if X // D > K:
        ans = X - D * K
    else:
        if (K - X // D) % 2 == 0:
            ans = X % D
        else:
            ans = D - X % D
    # output
    print(ans)

=======
Suggestion 8

def main():
    # input
    x, k, d = map(int, input().split())

    # compute

    # output
    print(0)

=======
Suggestion 9

def main():
    x,k,d = map(int, input().split())
    x = abs(x)
    if x - k*d >= 0:
        print(x - k*d)
    else:
        if (x//d) % 2 == k % 2:
            print(x % d)
        else:
            print(abs(x % d - d))

=======
Suggestion 10

def solve():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x/d > k:
        return x - d*k
    else:
        k -= x//d
        x = x%d
        if k%2 == 0:
            return x
        else:
            return d-x

print(solve())
