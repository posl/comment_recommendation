Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, n = map(int, input().split())
    ans = 0
    while n > 0:
        if n % 3 == 0:
            ans += (n // 3) * y
            n = 0
        else:
            ans += x
            n -= 1
    print(ans)

=======
Suggestion 2

def main():
    x, y, n = map(int, input().split())
    ans = 0
    while n > 0:
        if n % 3 == 0:
            ans += y * (n // 3)
            n = 0
        else:
            ans += x
            n -= 1
    print(ans)

=======
Suggestion 3

def main():
    X, Y, N = map(int, input().split())
    ans = 0
    while N > 0:
        if N % 3 == 0:
            ans += Y * (N // 3)
            N = 0
        else:
            ans += X
            N -= 1
    print(ans)

=======
Suggestion 4

def main():
    x, y, n = map(int, input().split())
    cost = 0
    while n > 0:
        if n >= 3:
            n -= 3
            cost += y
        else:
            n -= 1
            cost += x
    print(cost)

=======
Suggestion 5

def main():
    x, y, n = map(int, input().split())
    ans = 0
    if n % 2 == 0:
        ans = n // 2 * min(x * 2, y)
    else:
        ans = (n // 2) * min(x * 2, y) + x
    print(ans)

=======
Suggestion 6

def main():
    x, y, n = map(int, input().split())
    #print(x, y, n)
    apple = 0
    money = 0
    while apple < n:
        if (n - apple) % 3 == 0:
            money += y
            apple += 3
        else:
            money += x
            apple += 1
    print(money)

=======
Suggestion 7

def main():
    x, y, n = map(int, input().split())
    print(n * x if n < 3 else n * x + (n // 3) * (y - x))

=======
Suggestion 8

def main():
    X, Y, N = map(int, input().split())
    # print(X, Y, N)
    # print(type(X), type(Y), type(N))
    # print(X * (N % 3) + Y * (N // 3))
    print(X * (N % 3) + Y * (N // 3))

=======
Suggestion 9

def main():
    # 入力
    X, Y, N = map(int, input().split())
    # 処理
    # 1個のりんごを買うときの最小金額を求める
    min_cost = min(X, Y)
    # 3個のりんごを買うときの最小金額を求める
    min_cost3 = min(X*3, Y)
    # 3個のりんごを買うときの最小金額から1個のりんごを買うときの最小金額を引く
    min_cost1 = min_cost3 - min_cost
    # 3個のりんごを買うときの最小金額から1個のりんごを買うときの最小金額を引く
    min_cost2 = min_cost3 - min_cost
    # 3個のりんごを買うときの最小金額から1個のりんごを買うときの最小金額を引く
    min_cost3 = min_cost3 - min_cost
    # 3個のりん

=======
Suggestion 10

def main():
    X, Y, N = map(int, input().split())
    #X円払って1個のりんごを手に入れる操作をN個するのが最適かX円払って3個のりんごを手に入れる操作をN/3個するのが最適かを判定
    #X円払って1個のりんごを手に入れる操作をN個するのが最適な場合
    if X * N < Y * (N // 3):
        print(X * N)
    #X円払って3個のりんごを手に入れる操作をN/3個するのが最適な場合
    else:
        print(Y * (N // 3) + X * (N % 3))
