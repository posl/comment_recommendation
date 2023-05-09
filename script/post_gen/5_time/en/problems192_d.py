Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = input()
    m = int(input())
    d = int(max(x))
    if len(x) == 1:
        if int(x) <= m:
            print(1)
        else:
            print(0)
    else:
        l = d + 1
        r = m + 1
        if l == r:
            print(1)
        else:
            while r - l > 1:
                mid = (l + r) // 2
                val = 0
                for i in range(len(x)):
                    val += int(x[len(x) - i - 1]) * (mid ** i)
                if val <= m:
                    l = mid
                else:
                    r = mid
            print(l - d)

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

    # 二分探索
    l = d + 1
    r = m + 1
    while r - l > 1:
        mid = (l + r) // 2
        if x2num(x, mid) <= m:
            l = mid
        else:
            r = mid

    print(l - d)

=======
Suggestion 3

def baseN(num, b):
    return ((num == 0) and "0") or (baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])

X = input()
M = int(input())

d = max([int(c) for c in X])

ans = 0
while True:
    try:
        n = baseN(M, d+1)
        if len(n) > len(X):
            break
        ans += 1
        M += 1
    except:
        break

print(ans)

=======
Suggestion 4

def main():
    X = input()
    M = int(input())
    d = max([int(c) for c in X])
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        return
    def f(n):
        r = 0
        for c in X:
            r = r * n + int(c)
            if r > M:
                return False
        return True
    l = d + 1
    r = 10 ** 18 + 1
    while l + 1 < r:
        m = (l + r) // 2
        if f(m):
            l = m
        else:
            r = m
    print(l - d)

main()

=======
Suggestion 5

def main():
    x = input()
    m = int(input())
    d = max([int(i) for i in x])
    l = len(x)
    if l == 1:
        print(1 if int(x) <= m else 0)
        return
    else:
        n = d + 1
        while True:
            t = 0
            for i in range(l):
                t += n ** (l - i - 1) * int(x[i])
                if t > m:
                    break
            if t > m:
                break
            n += 1
        print(n - d - 1)

=======
Suggestion 6

def get_max_digit(s):
    max_digit = 0
    for i in range(len(s)):
        if int(s[i]) > max_digit:
            max_digit = int(s[i])
    return max_digit

=======
Suggestion 7

def f(s, n):
    v = 0
    for i in s:
        v = v * n + int(i)
        if v > m:
            return False
    return True

s = input()
m = int(input())

d = int(max(s))

=======
Suggestion 8

def base_n(x, n):
    ans = 0
    for i in range(len(x)):
        ans += int(x[-i-1]) * pow(n, i)
    return ans

x = input()
m = int(input())

=======
Suggestion 9

def main():
    x = input()
    m = int(input())

    d = int(max(x))
    ans = 0
    while True:
        try:
            ans += int(x, d+1) <= m
            d += 1
        except ValueError:
            break

    print(ans)

main()

=======
Suggestion 10

def main():
    X = input()
    M = int(input())
    d = int(max(X))
    ans = 0
    for i in range(d+1,M+1):
        n = int(X, i)
        if ans < n <= M:
            ans = n
    print(ans)
