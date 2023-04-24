Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = x[1] - x[0]
    for i in range(N):
        d = gcd(d, x[i+1] - x[i])
    print(d)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = []
    for i in range(N):
        d.append(x[i+1] - x[i])
    d.sort()
    g = d[0]
    for i in range(1, N):
        g = gcd(d[i], g)
    print(g)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = abs(x[0] - x[1])
    for i in range(1, N + 1):
        d = gcd(d, abs(x[i] - x[i + 1]))
    print(d)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    x_diff = [x[i+1] - x[i] for i in range(N)]
    #print(x_diff)
    #print("N:", N)
    #print("X:", X)
    #print("x:", x)
    #print("x_diff:", x_diff)
    if N == 1:
        print(x_diff[0])
    else:
        D = x_diff[0]
        for i in range(1, N):
            D = gcd(D, x_diff[i])
        print(D)

=======
Suggestion 5

def main():
    # input
    N, X = map(int, input().split())
    xs = list(map(int, input().split()))

    # compute
    ds = [abs(X-x) for x in xs]
    d = ds[0]
    for i in range(1, N):
        d = gcd(d, ds[i])

    # output
    print(d)

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.sort()
    diff_list = []
    for i in range(n-1):
        diff_list.append(x_list[i+1] - x_list[i])
    diff_list.sort()
    diff = diff_list[0]
    for i in range(n-1):
        diff = gcd(diff, diff_list[i])
    print(diff)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    # print(x)
    # print(x[-1])
    # print(x[0])
    # print(x[-1] - x[0])
    # print(x[-1] - x[0])
    D = x[-1] - x[0]
    for i in range(1, N):
        # print(x[-1] - x[i])
        # print(x[i] - x[0])
        D = min(D, x[-1] - x[i], x[i] - x[0])
        # print(D)
    # print(D)
    print(D)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))

    # Xとxの差を取得
    x = [abs(X - i) for i in x]

    # 一番小さい値を取得
    ans = min(x)

    # 2つの値の最大公約数を求める
    for i in x:
        ans = gcd(ans, i)

    print(ans)

=======
Suggestion 9

def main():
    N,X = map(int,input().split())
    x = list(map(int,input().split()))
    #print(N,X,x)
    #print(abs(X-x[0]))
    d = abs(X-x[0])
    for i in range(N):
        d = gcd(d,abs(X-x[i]))
    print(d)
