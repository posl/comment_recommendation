Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if K*D <= X:
        print(X-K*D)
        return
    K -= X//D
    X %= D
    if K%2 == 0:
        print(X)
    else:
        print(D-X)

=======
Suggestion 2

def problems175_c():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k * d:
        print(x - k * d)
        return
    if (k - x // d) % 2 == 0:
        print(x % d)
        return
    print(d - x % d)

=======
Suggestion 3

def main():
    x,k,d = map(int, input().split())
    x = abs(x)
    if x - k*d >= 0:
        print(x-k*d)
    else:
        if (x//d)%2 == k%2:
            print(x%d)
        else:
            print(d-x%d)

=======
Suggestion 4

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k * d:
        print(x - k * d)
    else:
        k -= x // d
        x = x % d
        if k % 2 == 0:
            print(x)
        else:
            print(d - x)

=======
Suggestion 5

def main():
    x,k,d = map(int, input().split())
    x = abs(x)
    if x//d > k:
        print(x-k*d)
    else:
        k = k - x//d
        x = x%d
        if k%2 == 0:
            print(x)
        else:
            print(d-x)

=======
Suggestion 6

def main():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x >= k*d:
        print(x-k*d)
        return
    else:
        k = k - x//d
        x = x%d
        if k%2 == 0:
            print(x)
        else:
            print(d-x)

=======
Suggestion 7

def main():
    X, K, D = map(int, input().split())
    if X > 0:
        if X - K * D > 0:
            print(X - K * D)
        else:
            print(abs(X - K * D))
    elif X < 0:
        if X + K * D < 0:
            print(abs(X + K * D))
        else:
            print(X + K * D)
    else:
        print(abs(X + K * D))

=======
Suggestion 8

def problem175_c():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= d * k:
        print(x - d * k)
        return
    n = x // d
    if (k - n) % 2 == 0:
        print(x - n * d)
    else:
        print(d - x + n * d)

=======
Suggestion 9

def main():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x > k*d:
        print(x-k*d)
    else:
        t = x//d
        if (k-t)%2==0:
            print(x%d)
        else:
            print(d-x%d)

=======
Suggestion 10

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
