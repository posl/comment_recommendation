Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = input()
    m = int(input())

    if len(x) == 1:
        if int(x) <= m:
            print(1)
        else:
            print(0)
        return

    d = int(max(x))
    x = [int(i) for i in x]

    def base_n(x, n):
        x = x[::-1]
        result = 0
        for i in range(len(x)):
            result += x[i] * n**i
        return result

    def check(n):
        return base_n(x, n) <= m

    def binary_search():
        left = d + 1
        right = m + 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1

    print(binary_search() - d)

=======
Suggestion 2

def convert(x, n):
    if x == 0:
        return '0'
    result = ''
    while x > 0:
        result = str(x % n) + result
        x //= n
    return result

X = input()
M = int(input())

d = int(max(list(X)))

=======
Suggestion 3

def main():
    x = input()
    m = int(input())
    d = int(max(x))
    l = len(x)

    if l == 1:
        if int(x) <= m:
            print(1)
        else:
            print(0)
        return

    def base_n_to_10(x, n):
        out = 0
        for i in range(1,len(str(x))+1):
            out += int(x[-i])*(n**(i-1))
        return out

    def is_ok(arg):
        if base_n_to_10(x, arg) <= m:
            return True
        else:
            return False

    def meguru_bisect(ng, ok):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(meguru_bisect(m+1, d+1)-d)

=======
Suggestion 4

def main():
    x = input()
    m = int(input())
    d = int(max(x))
    #print(d)
    def base_n(x, n):
        if (int(x / n)):
            return base_n(int(x / n), n) + str(x % n)
        return str(x % n)
    def is_ok(v):
        if m < int(v):
            return False
        return True
    def binary_search():
        ng = 0
        ok = 10**18
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(base_n(int(x), mid)):
                ng = mid
            else:
                ok = mid
        return ok
    print(binary_search() - d)

=======
Suggestion 5

def main():
    X = input()
    M = int(input())
    l = len(X)
    d = int(max(X))
    if l == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
    else:
        def digit(n):
            if n < 10:
                return 1
            else:
                return 1 + digit(n//10)
        def convert(n, d):
            l = digit(n)
            s = 0
            for i in range(l):
                s += n%10 * pow(d, i)
                n //= 10
            return s
        def check(n):
            if convert(n, d+1) <= M:
                return True
            else:
                return False
        def binary_search():
            ok = M+1
            ng = 0
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if check(mid):
                    ng = mid
                else:
                    ok = mid
            return ok - M
        print(binary_search())

=======
Suggestion 6

def convert_base(n, b):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(str(n % b))
        n //= b
    return ''.join(digits[::-1])

X = input()
M = int(input())
d = int(max(X))

=======
Suggestion 7

def solve(X, M):
    d = int(max(X))
    if len(X) == 1:
        if int(X) <= M:
            return 1
        else:
            return 0
    else:
        #Xを10進法表記とみなして得られる値を求める
        X10 = 0
        for i in range(len(X)):
            X10 += int(X[i]) * (d ** (len(X)-i-1))
        #XをXの最大値+1進法表記とみなして得られる値を求める
        X11 = 0
        for i in range(len(X)):
            X11 += int(X[i]) * ((d+1) ** (len(X)-i-1))
        #XをXの最大値+2進法表記とみなして得られる値を求める
        X12 = 0
        for i in range(len(X)):
            X12 += int(X[i]) * ((d+2) ** (len(X)-i-1))
        #XをXの最大値+3進法表記とみなして得られる値を求める
        X13 = 0
        for i in range(len(X)):
            X13 += int(X[i]) * ((d+3) ** (len(X)-i-1))
        #XをXの最大値+4進法表記とみなして得られる値を求める
        X14 = 0
        for i in range(len(X)):
            X14 += int(X[i]) * ((d+4) ** (len(X)-i-1))
        #XをXの最大値+5進法表記とみなして得られる値を求める
        X15 = 0
        for i in range(len(X)):
            X15 += int(X[i]) * ((d+5) ** (len(X)-i-1))
        #XをXの最大値+6進法表記とみなして得られる値を求める
        X16 = 0
        for i in range(len

=======
Suggestion 8

def main():
    x = input()
    m = int(input())
    d = int(max(x))
    if len(x) == 1:
        if int(x) <= m:
            print(1)
            return
        else:
            print(0)
            return
    else:
        def convert_base(x, base):
            if int(x) == 0:
                return 0
            else:
                digits = []
                while x:
                    digits.append(int(x % base))
                    x //= base
                digits.reverse()
                return int(''.join(map(str, digits)))
        n = d + 1
        while True:
            if convert_base(x, n) <= m:
                n += 1
            else:
                print(n - d - 1)
                return

=======
Suggestion 9

def main():
    x = input()
    m = int(input())
    d = int(max(x))
    n = d + 1
    while int(x, n) <= m:
        n += 1
    print(n - d - 1)

=======
Suggestion 10

def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

X = input()
M = int(input())
d = max([int(x) for x in X])
d = d + 1
l = len(X)
