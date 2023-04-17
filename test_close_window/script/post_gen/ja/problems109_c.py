Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = x[1] - x[0]
    for i in range(1, N):
        d = gcd(d, x[i + 1] - x[i])
    print(d)

=======

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    D = x[1] - x[0]
    for i in range(1, N+1):
        D = gcd(D, x[i+1] - x[i])
    print(D)

=======

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    d = x[1] - x[0]
    for i in range(2, N):
        d = gcd(d, x[i] - x[i - 1])
    print(d)

=======

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    ans = 0
    for i in range(N):
        ans = gcd(ans, abs(x[i] - X))
    print(ans)

=======

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    #print(N, X, x)
    if N == 1:
        print(abs(X - x[0]))
        exit()
    x.append(X)
    x.sort()
    #print(x)
    d = x[1] - x[0]
    for i in range(2, N + 1):
        d = gcd(d, x[i] - x[i - 1])
    print(d)

=======

def main():
    import sys
    input = sys.stdin.readline
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [abs(x - i) for i in a]
    a.sort()
    ans = a[0]
    for i in a:
        ans = gcd(ans, i)
    print(ans)

=======

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    #print(x)
    #print(x[0])
    #print(x[N-1])
    if N == 1:
        print(abs(X - x[0]))
        return
    if N == 2:
        print(min(abs(X - x[0]), abs(X - x[1])))
        return
    #print(x)
    d = x[1] - x[0]
    for i in range(1, N-1):
        d = gcd(d, x[i+1] - x[i])
    #print(d)
    print(min(abs(X - x[0]) % d, d - abs(X - x[0]) % d))

=======

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    # 1. Xと各xの差を求める
    # 2. 1で求めた差の最大公約数を求める
    # 3. 2で求めた最大公約数の最大値を求める
    # 4. 3で求めた最大値を出力する
    diff = list(map(lambda i: abs(X - i), x))
    gcd = diff[0]
    for i in range(1, len(diff)):
        gcd = math.gcd(gcd, diff[i])
    print(gcd)
