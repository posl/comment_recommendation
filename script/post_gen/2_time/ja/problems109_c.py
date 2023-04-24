Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = x[1] - x[0]
    for i in range(1, N + 1):
        d = gcd(d, x[i] - x[i - 1])
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
    ans = d[0]
    for i in range(1, N):
        ans = gcd(ans, d[i])
    print(ans)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = [x[i+1]-x[i] for i in range(N)]
    d.sort()
    ans = d[0]
    for i in range(1, N):
        ans = gcd(ans, d[i])
    print(ans)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    d = abs(x[0] - X)
    for i in range(1, N):
        d = gcd(d, abs(x[i] - X))
    print(d)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    diff = []
    for i in range(N):
        diff.append(abs(x[i] - X))
    #print(diff)
    #print(gcd_list(diff))
    print(gcd_list(diff))

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    #Xとの距離を求める
    x = [abs(i - X) for i in x]
    #Xとの距離の最大公約数を求める
    from math import gcd
    ans = x[0]
    for i in range(1, N):
        ans = gcd(ans, x[i])
    print(ans)

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))

    x_list.sort()
    x_list = [abs(x - i) for i in x_list]
    x_list = [i for i in x_list if i != 0]

    if len(x_list) == 0:
        print(0)
        return

    ans = x_list[0]
    for i in range(1, len(x_list)):
        ans = gcd(ans, x_list[i])

    print(ans)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))

    x.append(X)
    x.sort()

    # x[i]とx[i+1]の差の最大公約数を求める
    diff = [x[i+1]-x[i] for i in range(N)]
    g = diff[0]
    for i in range(1, N):
        g = gcd(g, diff[i])

    print(g)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    print(max([max([x[i] - X, X - x[i]]) for i in range(N)]) // 2)

=======
Suggestion 10

def main():
    #入力
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()

    #X と x[0] の差の最大公約数を求める
    d = x[0] - X
    for i in range(1, N):
        d = gcd(d, x[i] - X)
    
    #出力
    print(d)
