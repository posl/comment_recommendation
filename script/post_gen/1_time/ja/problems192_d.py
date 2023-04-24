Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return

    left = d
    right = M + 1
    while right - left > 1:
        mid = (left + right) // 2
        if check(X, mid, M):
            left = mid
        else:
            right = mid
    print(left - d)

=======
Suggestion 2

def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    l = 0
    r = M
    while r - l > 1:
        m = (l + r) // 2
        if int(X, m) <= M:
            l = m
        else:
            r = m
    if d + 1 <= l:
        print(l - d)
    else:
        print(0)

=======
Suggestion 3

def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
    else:
        left = d
        right = M+1
        while right - left > 1:
            mid = (left + right) // 2
            tmp = 0
            for i in range(len(X)):
                tmp *= mid
                tmp += int(X[i])
                if tmp > M:
                    break
            if tmp <= M:
                left = mid
            else:
                right = mid
        print(left - d)

=======
Suggestion 4

def main():
    X = input()
    M = int(input())
    N = len(X)
    d = int(max(X))

    if N == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return

    ok = d
    ng = M + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        s = 0
        for i in range(N):
            s = s * mid + int(X[i])
            if s > M:
                break
        if s <= M:
            ok = mid
        else:
            ng = mid
    print(ok - d)

=======
Suggestion 5

def main():
    X = input()
    M = int(input())
    d = max([int(x) for x in X])
    if len(X) == 1:
        if d > M:
            print(0)
        else:
            print(1)
        return
    left = d
    right = M + 1
    while right - left > 1:
        mid = (left + right) // 2
        tmp = 0
        for i in range(len(X)):
            tmp = tmp * mid + int(X[i])
            if tmp > M:
                break
        if tmp > M:
            right = mid
        else:
            left = mid
    print(left - d)

=======
Suggestion 6

def main():
    X = input()
    M = int(input())
    d = max([int(X[i]) for i in range(len(X))])
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return

    def is_ok(n):
        ans = 0
        for i in range(len(X)):
            ans += int(X[i]) * (n ** (len(X) - i - 1))
        return ans <= M

    def meguru_bisect(ng, ok):
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(meguru_bisect(d, M + 1) - d)

=======
Suggestion 7

def main():
    X = input()
    M = int(input())
    d = int(max(X))
    # d+1以上の整数nを選んでXをn進法表記の数とみなして得られる値のうち、M以下であるようなものは何種類あるか
    # 1 ≦ M ≦ 10^{18}
    # Xの最大値は9なので、nは9以下
    # 1 ≦ n ≦ 9
    # 1 ≦ n ≦ d+1
    # 1 ≦ n ≦ max(X)+1
    # nは整数である必要があるので、nはmax(X)+1以下の整数
    # 1 ≦ n ≦ max(X)+1
    # nは整数である必要があるので、nはfloor(max(X)+1)以下の整数
    # 1 ≦ n ≦ floor(max(X)+1)
    # nは整数である必要があるので、nはfloor(max(X))+1以下の整数
    # 1 ≦ n ≦ floor(max(X))
    # nは整数である必要があるので、nはfloor(max(X))以下の整数
    # 1 ≦ n ≦ floor(max(X))
    # nは整数である必要があるので、nはfloor(max(X))-1以下の整数
    # 1 ≦ n ≦ floor(max(X))-1
    # nは整数である必要があるので、nはfloor(max(X))-1以下の整数
    # 1 ≦ n ≦ floor(max(X))-1
    # nは整数である必要があるので、nはfloor(max(X))-1以下の整数
    # 1 ≦ n ≦ floor(max(X))-1
    # nは整数である必要があるので、nはfloor(max(X))-1以下の整数
    # 1 ≦ n ≦ floor(max(X))-1
    # n

=======
Suggestion 8

def main():
    x = input()
    m = int(input())
    n = len(x)
    #print(x,m,n)
    d = 0
    for i in range(n):
        d = max(d,int(x[i]))
    #print(d)
    if d == 1:
        print(n)
        exit()
    l = d
    r = m+1
    while r-l>1:
        mid = (r+l)//2
        #print(mid)
        v = 0
        for i in range(n):
            v = v*mid + int(x[i])
        if v>m:
            r = mid
        else:
            l = mid
    print(l-d)

=======
Suggestion 9

def main():
    X = input()
    M = int(input())
    #Xを10進数で見たときの最大の数
    max = 0
    for i in X:
        if max < int(i):
            max = int(i)
    #max+1以上の数で、Xをn進数で見たときの数がM以下のnの個数をカウント
    count = 0
    for i in range(max+1, M+1):
        total = 0
        for j in range(len(X)):
            total += int(X[j]) * pow(i, len(X)-j-1)
        if total <= M:
            count += 1
    #M以下の数の個数
    print(count)

=======
Suggestion 10

def main():
    X = input()
    M = int(input())
    X = list(map(int, X))
    X.sort()
    X.reverse()
    d = X[0]

    # d+1以上の最小のnを求める
    n = d+1
    while True:
        if n**len(X) > M:
            break
        n += 1

    # n進法で表現したときの最小の値を求める
    min_n = 0
    for i in range(len(X)):
        min_n += X[i] * (n**i)

    # n進法で表現したときの最大の値を求める
    max_n = 0
    for i in range(len(X)):
        max_n += X[i] * (n**(len(X)-i-1))

    # 最小の値がM以下の場合、答えは1
    if min_n <= M:
        print(1)
        return

    # Mがn進法で表現したときの最小の値と最大の値の間にある場合、答えは2
    if min_n <= M and M <= max_n:
        print(2)
        return

    # Mがn進法で表現したときの最大の値より大きい場合、答えは0
    if M < min_n:
        print(0)
        return
