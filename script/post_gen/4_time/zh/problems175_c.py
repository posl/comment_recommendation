Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if X//D >= K:
        print(X-D*K)
    else:
        K -= X//D
        X %= D
        if K%2 == 0:
            print(X)
        else:
            print(D-X)

=======
Suggestion 2

def solve(x,k,d):
    if x < 0:
        x = -x
    if x//d >= k:
        return x - k*d
    else:
        return solve(x%d, k - x//d, d)

x, k, d = map(int, input().split())
print(solve(x,k,d))

=======
Suggestion 3

def problem175_c():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x//d >= k:
        print(x-k*d)
    else:
        x = x%d
        k = k-x//d
        if k%2 == 0:
            print(x)
        else:
            print(d-x)

=======
Suggestion 4

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x//d >= k:
        print(x-d*k)
    else:
        k -= x//d
        x %= d
        if k % 2 == 0:
            print(x)
        else:
            print(d-x)

=======
Suggestion 5

def calc(x, k, d):
    if x < 0:
        x = -x
    if x >= k * d:
        return x - k * d
    else:
        y = x % d
        if (k - x // d) % 2 == 0:
            return y
        else:
            return d - y

x, k, d = map(int, input().split())
print(calc(x, k, d))

=======
Suggestion 6

def main():
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
Suggestion 7

def main():
    X,K,D = map(int,input().split())
    X = abs(X)
    if X//D > K:
        print(X-K*D)
    else:
        if (K-X//D)%2 == 0:
            print(X%D)
        else:
            print(D-X%D)

=======
Suggestion 8

def problem175_c():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x >= k*d:
        print(x-k*d)
    else:
        y = x//d
        if (k-y)%2 == 0:
            print(x%d)
        else:
            print(abs(x%d-d))

=======
Suggestion 9

def main():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x/d > k:
        print(x-d*k)
    else:
        k -= x//d
        x %= d
        if k%2 == 0:
            print(x)
        else:
            print(abs(x-d))

=======
Suggestion 10

def main():
    x,k,d = map(int, input().split())
    x = abs(x)
    if x - k*d >= 0:
        print(x - k*d)
    else:
        m = x // d
        if (k-m) % 2 == 0:
            print(x - m*d)
        else:
            print(abs(x - (m+1)*d))
