Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
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
Suggestion 2

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
Suggestion 3

def main():
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
Suggestion 4

def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if X // D >= K:
        print(X - D * K)
        return
    K -= X // D
    X %= D
    if K % 2 == 0:
        print(X)
    else:
        print(abs(X - D))

=======
Suggestion 5

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    ans = 0
    if x - k * d >= 0:
        ans = x - k * d
    else:
        if (k - x // d) % 2 == 0:
            ans = x % d
        else:
            ans = d - x % d
    print(ans)

=======
Suggestion 6

def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if X >= K*D:
        print(X-K*D)
    else:
        K -= X//D
        X = X%D
        if K%2 == 0:
            print(X)
        else:
            print(D-X)

=======
Suggestion 7

def main():
    X,K,D = map(int,input().split())
    X = abs(X)
    if X >= K*D:
        print(X-K*D)
    else:
        K -= X//D
        X %= D
        if K%2 == 0:
            print(X)
        else:
            print(abs(X-D))

=======
Suggestion 8

def main():
    #input
    X, K, D = map(int, input().split())
    #compute
    X = abs(X)
    if K*D <= X:
        ans = X - K*D
    else:
        K -= X//D
        X = X%D
        if K%2 == 1:
            ans = abs(X-D)
        else:
            ans = X
    #output
    print(ans)

=======
Suggestion 9

def main():
    x,k,d = map(int,input().split())
    x = abs(x)
    num = x//d
    if k <= num:
        ans = x - k * d
    else:
        if (k - num) % 2 == 0:
            ans = x - num * d
        else:
            ans = abs(x - (num+1) * d)
    print(ans)

=======
Suggestion 10

def main():
    x, k, d = map(int, input().split())

    x = abs(x)

    # 1. xがdより小さい場合はx - d*kの絶対値を出力
    if x < d:
        print(abs(x - d*k))
        return

    # 2. xがdより大きい場合は、xをdで割った余りを出力
    if x >= d:
        if x % d > 0:
            if k % 2 == 0:
                print(x % d)
                return
            else:
                print(abs((x % d) - d))
                return
        else:
            if k % 2 == 0:
                print(x % d)
                return
            else:
                print(abs((x % d) - d))
                return
