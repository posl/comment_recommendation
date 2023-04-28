Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x // d >= k:
        print(x - k * d)
        return
    k -= x // d
    x %= d
    if k % 2 == 0:
        print(x)
    else:
        print(d - x)

=======
Suggestion 2

def solve():
    # -*- coding: utf-8 -*-
    # 整数の入力
    #a = int(input())
    # スペース区切りの整数の入力
    #b, c = map(int, input().split())
    # 文字列の入力
    #s = input()
    # 出力
    #print("{} {}".format(a+b+c, s))
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= d * k:
        print(x - d * k)
    else:
        if (k - x // d) % 2 == 0:
            print(x % d)
        else:
            print(d - x % d)
    return 0

=======
Suggestion 3

def main():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x//d >= k:
        print(x-k*d)
    else:
        k -= x//d
        x %= d
        if k%2 == 0:
            print(x)
        else:
            print(d-x)

=======
Suggestion 4

def main():
    x, k, d = map(int, input().split())

    x = abs(x)
    if x >= d * k:
        print(x - d * k)
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
    x, k, d = map(int, input().split())
    x = abs(x)
    if x - k * d > 0:
        print(x - k * d)
        return
    else:
        if (x - k * d) % (2 * d) == 0:
            print(0)
            return
        else:
            print(abs((x - k * d) % (2 * d) - 2 * d))
            return

=======
Suggestion 6

def sol():
    X, K, D = map(int, input().split())
    X = abs(X)
    if X // D >= K:
        print(X - D * K)
    else:
        K -= X // D
        X %= D
        if K % 2 == 0:
            print(X)
        else:
            print(D - X)

=======
Suggestion 7

def main():
    # input
    X, K, D = map(int, input().split())

    # compute
    if X < 0:
        X = -X
    if X//D >= K:
        print(X-K*D)
    else:
        if (K-X//D)%2 == 0:
            print(X%D)
        else:
            print(D-X%D)

=======
Suggestion 8

def solve():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x >= k*d:
        return x - k*d
    else:
        k -= x//d
        x = x%d
        if k%2 == 0:
            return x
        else:
            return d - x

=======
Suggestion 9

def solve():
    X,K,D = map(int,input().split())
    X = abs(X)
    if X//D >= K:
        return X-K*D
    else:
        K -= X//D
        X -= (X//D)*D
        if K%2 == 0:
            return X
        else:
            return D-X

=======
Suggestion 10

def solve(x,k,d):
    if x < 0:
        x = -1 * x
    if x >= k*d:
        return x - k*d
    else:
        n = x//d
        x -= n*d
        k -= n
        if k%2 == 0:
            return x
        else:
            return d-x

x,k,d = map(int,input().split())
print(solve(x,k,d))
