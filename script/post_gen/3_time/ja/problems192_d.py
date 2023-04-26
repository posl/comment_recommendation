Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X = input()
    M = int(input())
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        return
    d = max(X)
    d = int(d)
    l = d + 1
    r = 10**18 + 1
    while r - l > 1:
        mid = (l + r) // 2
        num = 0
        for i in range(len(X)):
            num *= mid
            num += int(X[i])
        if num <= M:
            l = mid
        else:
            r = mid
    print(l - d)

=======
Suggestion 2

def main():
    X = input()
    M = int(input())

    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        return

    X = [int(x) for x in X]
    D = max(X)
    X = X[::-1]

    l, r = D+1, 10**18+1

    while r - l > 1:
        m = (l + r) // 2
        v = 0
        for i in range(len(X)):
            v += X[i] * m ** i
        if v <= M:
            l = m
        else:
            r = m

    print(l - D)

=======
Suggestion 3

def main():
    X = input()
    M = int(input())

    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        return

    # Xをn進法表記とみなして得られる値のうちM以下であるようなものは何種類あるか
    # Xをn進法表記とみなして得られる値のうちM以下であるようなものは何種類あるか
    # Xをn進法表記とみなして得られる値のうちM以下であるようなものは何種類あるか
    # Xをn進法表記とみなして得られる値のうちM以下であるようなものは何種類あるか
    # Xをn進法表記とみなして得られる値のうちM以下であるようなものは何種類あるか
    # Xをn進法表記とみなして得られる値のうちM以下であるようなものは何種類あるか
    # Xをn進法表記とみなして得られる値のうちM以下であるようなものは何種類あるか
    # Xをn進法表記とみなして得られる値のうちM以下であるようなものは何種類あるか
    # Xをn進法表記とみなして得られる値のうちM以下であるようなものは何種類あるか
    # Xをn進法表記とみなして得られる値のうちM以下であるようなものは何種類あるか
    # Xをn進法表記とみなして得られる値のうちM

=======
Suggestion 4

def main():
    X = input()
    M = int(input())
    d = max([int(i) for i in X])
    if len(X) == 1:
        print(1 if int(X) <= M else 0)
        return
    left = d
    right = M + 1
    while right - left > 1:
        mid = (right + left) // 2
        if int(X, mid) > M:
            right = mid
        else:
            left = mid
    print(left - d)

=======
Suggestion 5

def main():
    X = input()
    M = int(input())
    d = max(X)
    d = int(d)
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    ng = 0
    ok = M + 1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if mid ** len(X) <= M:
            ng = mid
        else:
            ok = mid
    if d + 1 <= ok:
        print(ok - d - 1)
    else:
        print(0)

=======
Suggestion 6

def main():
    X = input()
    M = int(input())
    d = max(map(int, X))
    if len(X) == 1:
        print(1 if d <= M else 0)
        return
    ok = d
    ng = 10 ** 18 + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if int(X, mid) <= M:
            ok = mid
        else:
            ng = mid
    print(ok - d)

=======
Suggestion 7

def main():
    X = input()
    M = int(input())

    # X が 1 桁の場合
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        return

    # X が 2 桁以上の場合
    # X の各桁の数字を d とすると、 d+1 以上の整数 n で X を n 進法表記の数とみなして得られる値のうち、
    # M 以下であるようなものは、 d+1 以上の整数 n のうち、
    # n = d+1 となるもののみである。
    # したがって、 X の各桁の数字の最大値を d とすれば、
    # d+1 以上の整数 n のうち、
    # n = d+1 となるもののみである。
    print(int(X, int(max(X))) - int(X) + 1)

=======
Suggestion 8

def main():
    X = input()
    M = int(input())

    # X の最大の数字を求める
    d = 0
    for c in X:
        d = max(d, int(c))

    # X が 1 桁のときは M 以下の値が 1 つだけ存在する
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return

    # X が 2 桁以上のときは、d+1 以上の整数 n で X を n 進法表記の数とみなして得られる値のうち、M 以下であるようなものの数を求める
    # この値は d+1 以上 M 以下の整数のうち、d+1 以上の整数 n で X を n 進法表記の数とみなして得られる値のうち、M 以下であるようなものの数と等しい
    # そのため、d+1 以上 M 以下の整数のうち、X を d+1 以上の整数 n で n 進法表記の数とみなして得られる値のうち、M 以下であるようなものの数を求めればよい
    # X を d+1 以上の整数 n で n 進法表記の数とみなして得られる値のうち、M 以下であるようなものの数を求めるには、二分探索を用いる
    # 二分探索の範囲を [d+1, M] とする
    # 二分探索の中央の値 n で X を n 進法表記の数とみなして得られる値を求め、M 以下であるかどうかを判定する
    # このとき、X を n 進法表

=======
Suggestion 9

def main():
    X = input()
    M = int(input())

    #Xを10進法表記とみなして得られる値は、X
    #Xをn進法表記とみなして得られる値は、n進数
    #Xをn進法表記とみなして得られる値のうちM以下であるようなものは何種類あるか？

    #Xを10進法表記とみなして得られる値は、X
    #Xをn進法表記とみなして得られる値は、n進数
    #Xをn進法表記とみなして得られる値のうちM以下であるようなものは何種類あるか？

    #Xをn進法表記とみなして得られる値のうちM以下であるようなものは何種類あるか？
    #Xをn進法表記とみなして得られる値のうちM以下であるようなものは何種類あるか？
    #Xをn進法表記とみなして得られる値のうちM以下であるようなものは何種類あるか？
    #Xをn進法表記とみなして得られる値のうちM以下であるようなものは何種類あるか？
    #Xをn進法表記とみなして得られる値のうちM以下であるようなものは何種類あるか？
    #Xをn進法表記とみなして得られる値のうちM以下であるようなものは何種類あるか？
    #Xをn進法表記とみなして得られる値のうちM以下であるようなものは何種類ある

=======
Suggestion 10

def main():
    X = int(input())
    M = int(input())
    X = str(X)
    X = list(X)
    X = [int(i) for i in X]
    X = sorted(X,reverse=True)
    X = X[0]
    if X == 1:
        print(1)
        exit()
    if M < X:
        print(0)
        exit()
    else:
        left = X
        right = M + 1
        while (right - left) > 1:
            mid = (left + right) // 2
            num = 0
            for i in range(len(str(M))):
                num += (mid ** i) * int(str(M)[i])
            if num > M:
                right = mid
            else:
                left = mid
        print(left - X)
