Synthesizing 10/10 solutions

=======
Suggestion 1

def convert(s, base):
    x = 0
    for i in s:
        x = x * base + int(i)
    return x

=======
Suggestion 2

def f(x, m):
    d = int(max(x))
    ans = 0
    while True:
        if int(x, d+1) <= m:
            ans += 1
        else:
            break
        d += 1
    return ans


x = input()
m = int(input())
print(f(x, m))

=======
Suggestion 3

def solve(x, m):
    d = int(max(x))
    ans = 0
    for i in range(d + 1, 10):
        if int(x, i) <= m:
            ans += 1
    return ans

x = input()
m = int(input())
print(solve(x, m))

=======
Suggestion 4

def f(x, m):
    d = 0
    for i in x:
        d = max(d, int(i))
    l = d + 1
    r = m + 1
    while r - l > 1:
        mid = (l + r) // 2
        t = 0
        k = 1
        for i in range(len(x) - 1, -1, -1):
            t += k * int(x[i])
            k *= mid
        if t <= m:
            l = mid
        else:
            r = mid
    return l - d

x = input()
m = int(input())
print(f(x, m))

=======
Suggestion 5

def main():
    x = int(input())
    m = int(input())
    x = str(x)
    d = 0
    for i in x:
        if int(i) > d:
            d = int(i)
    n = d + 1
    while True:
        if int(x, n) > m:
            n -= 1
            break
        n += 1
    print(n - d)

=======
Suggestion 6

def get_int(num_str, base):
    num = 0
    for i in range(len(num_str)):
        num += int(num_str[i]) * (base ** (len(num_str) - i - 1))
    return num

=======
Suggestion 7

def get_value(x, base):
    value = 0
    for i in range(len(x)):
        value = value * base + int(x[i])
    return value

=======
Suggestion 8

def main():
    X = input()
    M = int(input())

    d = int(max(list(X)))
    X = list(X)
    X.reverse()
    X = [int(x) for x in X]

    if len(X) == 1:
        if X[0] <= M:
            print(1)
        else:
            print(0)
        return

    def convert(n):
        if n == 0:
            return 0
        base = d + 1
        result = 0
        for i in range(len(X)):
            result += X[i] * (base ** i)
        return result

    # 二分法
    left = d + 1
    right = M + 1
    while left < right:
        mid = (left + right) // 2
        if convert(mid) <= M:
            left = mid + 1
        else:
            right = mid
    print(left - d - 1)

=======
Suggestion 9

def solve(X, M):
    d = int(max(X))
    if len(X) == 1:
        if int(X) <= M:
            return 1
        else:
            return 0
    else:
        X = list(X)
        X = [int(i) for i in X]
        X = [i-d for i in X]
        X = [str(i) for i in X]
        X = ''.join(X)
        X = int(X, d+1)
        if X <= M:
            return 1
        else:
            return 0

X = input()
M = int(input())
ans = 0
while True:
    ans += solve(X, M)
    X = int(X)
    X += 1
    X = str(X)
    if len(X) == 1:
        X = '0' + X
    if int(X) > M:
        break
print(ans)

=======
Suggestion 10

def main():
    x = input()
    m = int(input())
    d = int(max(x))
    ans = 0
    for n in range(d+1, m+1):
        if int(x, n) <= m:
            ans += 1
    print(ans)
