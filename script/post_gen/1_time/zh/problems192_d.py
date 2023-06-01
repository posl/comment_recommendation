Synthesizing 10/10 solutions

=======
Suggestion 1

def f(x, n):
    if x == 0:
        return 0
    else:
        return f(x//n, n) + x%n

=======
Suggestion 2

def solve(x, m):
    if len(x) == 1:
        if int(x) <= m:
            return 1
        else:
            return 0
    d = int(max(x))
    ans = 0
    for i in range(d+1, 10):
        x_ = int(x, i)
        if x_ <= m:
            ans += 1
    return ans

=======
Suggestion 3

def base_n_to_10(X, n):
    # base n to base 10
    ans = 0
    for i in range(len(X)):
        ans += int(X[-(i+1)]) * n**i
    return ans

=======
Suggestion 4

def is_ok(s, m, base):
    if len(s) == 0:
        return 1
    n = int(s[0])
    if n == 0:
        return is_ok(s[1:], m, base)
    if n < base:
        return base ** (len(s) - 1)
    if n == base:
        return is_ok(s[1:], m, base) + int(s[1:], base) + 1
    if n > base:
        return int(base ** (len(s) - 1) + base ** (len(s) - 2)) * (n - 1) + is_ok(s[1:], m, base)

=======
Suggestion 5

def solve(X, M):
    d = int(max(X))
    n = 0
    for i in range(1, len(X) + 1):
        n += int(X[-i]) * pow(d + 1, i - 1)
    ans = 0
    while n <= M:
        ans += 1
        n += pow(d + 1, len(X) - 1)
    return ans

=======
Suggestion 6

def base_n_to_10(X, n):
    out = 0
    for i in X:
        out = out * n + int(i)
    return out

=======
Suggestion 7

def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
    else:
        def base_n_to_10(X, n):
            out = 0
            for i in range(1, len(X) + 1):
                out += int(X[-i]) * (n ** (i - 1))
            return out

        def base_10_to_n(x, n):
            out = ''
            while x > 0:
                out = str(x % n) + out
                x //= n
            return out

        def solve(X, M, d):
            if base_n_to_10(X, d + 1) > M:
                return 0
            else:
                n = d + 1
                while base_n_to_10(X, n) <= M:
                    n += 1
                return n - d - 1

        print(solve(X, M, d))

=======
Suggestion 8

def get_max_num(str):
    max_num = 0
    for s in str:
        if int(s) > max_num:
            max_num = int(s)
    return max_num

=======
Suggestion 9

def main():
    X = input()
    M = int(input())
    d = int(max(X))
    #print(X, M, d)
    def f(n, s):
        if s == 0:
            return 0
        else:
            return n * f(n, s - 1) + 1
    def g(n, s):
        if s == 0:
            return 0
        else:
            return n * g(n, s - 1) + n ** (s - 1)

    def h(n, s, m):
        if s == 0:
            return 0
        else:
            return n * h(n, s - 1, m) + min(n - 1, m // n ** (s - 1))

    def solve(n):
        if n == 0:
            return 1
        else:
            return h(n, len(X), M) - h(n, len(X) - 1, M)

    ans = 0
    for n in range(d + 1, 100):
        ans += solve(n)
    print(ans)

=======
Suggestion 10

def solve(x, m):
    # 二分查找
    if len(x) == 1:
        return 1 if int(x) <= m else 0
    # 二分查找
    min_base = int(max(x)) + 1
    max_base = m + 1
    while min_base < max_base:
        mid_base = (min_base + max_base) // 2
        num = 0
        for i in range(len(x)):
            num = num * mid_base + int(x[i])
            if num > m:
                break
        if num <= m:
            min_base = mid_base + 1
        else:
            max_base = mid_base
    return min_base - int(max(x))
