Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X,K,D = map(int,input().split())
    X = abs(X)
    if X//D >= K:
        print(X-K*D)
    else:
        K -= X//D
        X %= D
        if K%2 == 0:
            print(X)
        else:
            print(D-X)

=======
Suggestion 2

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k * d:
        print(x - k * d)
        return
    if (k - x // d) % 2 == 0:
        print(x % d)
    else:
        print(d - x % d)

=======
Suggestion 3

def problems175_c():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k * d:
        print(x - k * d)
    else:
        y = x % d
        if (k - x // d) % 2 == 0:
            print(y)
        else:
            print(d - y)

=======
Suggestion 4

def main():
    x,k,d = map(int,input().split())
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

def solve(x,k,d):
    x = abs(x)
    if x >= k*d:
        return x - k*d
    else:
        if (k*d-x)%2 == 0:
            return 0
        else:
            return min(abs(x-d),abs(x+d))

=======
Suggestion 6

def solve(x, k, d):
    x = abs(x)
    if x // d >= k:
        return x - k * d
    else:
        y = x % d
        k -= x // d
        if k % 2 == 0:
            return y
        else:
            return d - y

x, k, d = map(int, input().split())
print(solve(x, k, d))

=======
Suggestion 7

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x / d >= k:
        print(x - d * k)
    else:
        k -= x // d
        x %= d
        if k % 2 == 0:
            print(x)
        else:
            print(d - x)

=======
Suggestion 8

def main():
    x,k,d=map(int,input().split())
    x=abs(x)
    if x-k*d>=0:
        print(x-k*d)
    else:
        if (x//d)%2==k%2:
            print(x%d)
        else:
            print(d-(x%d))

=======
Suggestion 9

def main():
    x, k, d = map(int, input().split())

    x = abs(x)
    if k*d <= x:
        print(x-k*d)
        return

    if (k*d - x) % (2*d) == 0:
        print(0)
        return

    print(min(abs(x + d * (k - 2 * (x // d + 1))), abs(x - d * (k - 2 * (x // d + 1)))))

=======
Suggestion 10

def solve(x,k,d):
    if x < 0:
        x = -x
    if x >= k*d:
        return x-k*d
    else:
        y = x//d
        if (k-y)%2 == 0:
            return x-y*d
        else:
            return (y+1)*d-x
