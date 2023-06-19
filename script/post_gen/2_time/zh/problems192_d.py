Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读入数据
    X = input()
    M = in

=======
Suggestion 2

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
        l = d + 1
        r = M + 1
        while r - l > 1:
            m = (l + r) // 2
            if int(X, m) <= M:
                l = m
            else:
                r = m
        print(l - d)

=======
Suggestion 3

def main():
    X = input()
    M = int(input())
    d = int(max(X))
    n = d + 1
    X = int(X)
    count = 0
    while True:
        if X == 0:
            break
        count += 1
        X //= n
    print(count)

=======
Suggestion 4

def solve(x, m):
    d = int(max(x))
    l = len(x)
    if l == 1:
        if d <= m:
            return 1
        else:
            return 0
    else:
        # 二分法
        left = d
        right = m + 1
        while right - left > 1:
            mid = (left + right) // 2
            s = 0
            for i in range(l):
                s += int(x[i]) * (mid ** (l - i - 1))
            if s <= m:
                left = mid
            else:
                right = mid
        return left - d

=======
Suggestion 5

def solve(x,m):
    d = int(max(x))
    #print(d)
    ans = 0
    for i in range(d,m+1):
        if int(x,int(d+1))<=m:
            ans+=1
    print(ans)

x = input()
m = int(input())
solve(x,m)

=======
Suggestion 6

def get_val(a, b):
    c = 0
    for i in range(len(a)):
        c += int(a[i]) * pow(b, len(a) - i - 1)
    return c

x = input()
m = int(input())

d = 0
for i in range(len(x)):
    d = max(d, int(x[i]))

ans = 0
left = d + 1
right = m + 1
while (right - left > 1):
    mid = (left + right) // 2
    if (get_val(x, mid) <= m):
        left = mid
    else:
        right = mid
print(left - d)

=======
Suggestion 7

def solve(X, M):
    d = 0
    for c in X:
        d = max(d, int(c))
    if len(X) == 1:
        if int(X) <= M:
            return 1
        else:
            return 0
    l = d
    r = 10 ** 18 + 1
    while r - l > 1:
        m = (l + r) // 2
        if is_ok(X, M, m):
            l = m
        else:
            r = m
    return l - d

=======
Suggestion 8

def main():
    x = input()
    m = int(input())
    d = int(max(x))
    l = len(x)
    if l == 1:
        print(0 if int(x) > m else 1)
        return
    ans = 0
    for i in range(d+1, 10):
        if int(str(i) * l) <= m:
            ans += 1
    for i in range(1, l):
        ans += 9 * 10 ** (i-1)
    print(ans)

=======
Suggestion 9

def main():
    X = input()
    M = int(input())
    d = int(max(X))
    n = d + 1
    while int(X, n) <= M:
        n += 1
    print(n-d-1)

=======
Suggestion 10

def func(x, m):
    d = max([int(i) for i in x])
    x = int(x)
    if x <= m:
        return 1
    else:
        return 0

x = input()
m = int(input())
print(func(x, m))
