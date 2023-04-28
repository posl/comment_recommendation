Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X = input()
    M = int(input())
    if len(X) == 1:
        if int(X) <= M:
            print(1)
            return
        else:
            print(0)
            return
    else:
        d = int(max(list(X)))
        def base_n_to_10(X, n):
            out = 0
            for i in range(1,len(str(X))+1):
                out += int(X[-i])*(n**(i-1))
            return out
        
        def base_10_to_n(X, n):
            out = ''
            if (int(X/n)):
                out += base_10_to_n(int(X/n), n)
            out += str(X%n)
            return out
        
        def check(n):
            if n <= M:
                return True
            else:
                return False
        
        def binary_search(ok, ng):
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if check(base_n_to_10(X, mid)):
                    ok = mid
                else:
                    ng = mid
            return ok
        
        print(binary_search(0, M+1) - d)

=======
Suggestion 2

def main():
    x = input()
    m = int(input())
    d = int(max(x))
    if len(x) == 1:
        if int(x) <= m:
            print(1)
        else:
            print(0)
        return
    #二分探索
    def check(n):
        #Xをn進数としてみなす
        tmp = 0
        for i in range(len(x)):
            tmp += int(x[-1-i]) * n ** i
        if tmp <= m:
            return True
        else:
            return False
    #条件を満たす最大のnを二分探索で求める
    #nはd+1以上となる
    l = d+1
    r = 10 ** 18 + 1
    while r - l > 1:
        c = (l+r)//2
        if check(c):
            l = c
        else:
            r = c
    print(l - d)
    return

=======
Suggestion 3

def main():
    x = input()
    m = int(input())
    d = int(max(x))
    if len(x) == 1:
        if int(x) <= m:
            print(1)
        else:
            print(0)
        return
    l = d
    r = m + 1
    while r - l > 1:
        mid = (l + r) // 2
        v = 0
        for i in range(len(x)):
            v = v * mid + int(x[i])
            if v > m:
                break
        if v <= m:
            l = mid
        else:
            r = mid
    print(l - d)
main()

=======
Suggestion 4

def solve():
    X = input()
    M = int(input())

    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        return

    d = int(max(X))
    ans = 0
    l = d
    r = M + 1

    while r - l > 1:
        m = (l + r) // 2
        v = 0
        for x in X:
            v = v * m + int(x)
            if v > M:
                break
        if v <= M:
            l = m
        else:
            r = m

    print(l - d)

=======
Suggestion 5

def main():
    x = input()
    m = int(input())
    d = max([int(i) for i in x])
    if len(x) == 1:
        if int(x) <= m:
            print(1)
        else:
            print(0)
        exit()
    #print(d)
    l = d+1
    r = m+1
    while r-l > 1:
        mid = (l+r)//2
        #print(l, mid, r)
        if check(x, m, mid):
            l = mid
        else:
            r = mid
    print(l-d)

=======
Suggestion 6

def main():
    x = input()
    m = int(input())
    d = int(max(x))
    n = d+1
    while True:
        if int(x, n) > m:
            break
        n += 1
    print(n-d-1)

=======
Suggestion 7

def main():
    X = int(input())
    M = int(input())
    d = max([int(i) for i in str(X)])
    if X <= M:
        print(1)
        return
    if len(str(X)) == 1:
        print(0)
        return
    if M < d+1:
        print(0)
        return
    l = d+1
    r = M+1
    while l+1 < r:
        m = (l+r)//2
        s = 0
        for c in str(X):
            s = s*m + int(c)
            if s > M:
                break
        if s <= M:
            l = m
        else:
            r = m
    print(l-d)
    return

=======
Suggestion 8

def main():
    X = int(input())
    M = int(input())
    d = max(list(map(int, list(str(X)))))
    if X <= M:
        print(1)
        return
    l = d + 1
    r = 10 ** 18 + 1
    while r - l > 1:
        m = (l + r) // 2
        x = 0
        for i, c in enumerate(str(X)):
            x += int(c) * (m ** (len(str(X)) - i - 1))
            if x > M:
                break
        if x <= M:
            l = m
        else:
            r = m
    print(l - d)

=======
Suggestion 9

def convert_base(n, base):
    if n == 0:
        return "0"
    ret = ""
    while n > 0:
        ret += str(n % base)
        n //= base
    return ret[::-1]

=======
Suggestion 10

def convert_to_base_10(x, base):
    result = 0
    for i in range(len(x)):
        result += int(x[-(i+1)]) * (base ** i)
    return result

x = input()
m = int(input())
