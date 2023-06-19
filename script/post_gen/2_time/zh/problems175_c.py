Synthesizing 10/10 solutions

=======
Suggestion 1

def abs(x):
    if x >= 0:
        return x
    else:
        return -x

x, k, d = map(int, input().split())

x = abs(x)

=======
Suggestion 2

def main():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x >= k*d:
        print(x-k*d)
        return
    else:
        k -= x//d
        x %= d
        if k%2 == 0:
            print(x)
        else:
            print(d-x)
        return

=======
Suggestion 3

def main():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x/d >= k:
        print(x-d*k)
        return
    k -= x//d
    x %= d
    if k%2 == 0:
        print(x)
    else:
        print(abs(x-d))

=======
Suggestion 4

def solve():
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

solve()

=======
Suggestion 5

def solve():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x//d > k:
        return x-d*k
    else:
        k -= x//d
        x = x%d
        if k%2 == 0:
            return x
        else:
            return d-x

print(solve())

=======
Suggestion 6

def solve(x, k, d):
    x = abs(x)
    if x / d > k:
        return x - k * d
    else:
        k -= x / d
        x %= d
        if k % 2 == 0:
            return x
        else:
            return d - x

x, k, d = map(int, raw_input().split())
print solve(x, k, d)

=======
Suggestion 7

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if k*d <= x:
        print(x-k*d)
    else:
        t = x//d
        if (k-t)%2 == 0:
            print(x-t*d)
        else:
            print(d-(x-t*d))

=======
Suggestion 8

def input():
    x,k,d = map(int, input().split())
    return x,k,d

=======
Suggestion 9

def problems175_c():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x >= k*d:
        print(x-k*d)
    else:
        k = k - x//d
        x = x%d
        if k%2 == 0:
            print(x)
        else:
            print(d-x)

=======
Suggestion 10

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k * d:
        print(x - k * d)
        return
    if (k - x // d) % 2 == 0:
        print(x % d)
    else:
        print(abs(x % d - d))
