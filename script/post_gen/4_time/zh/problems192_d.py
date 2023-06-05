Synthesizing 10/10 solutions

=======
Suggestion 1

def f(x, m):
    d = int(max(x))
    return len([i for i in range(d+1, m+1) if int(x, d) >= i])

x = input()
m = int(input())
print(f(x, m))

=======
Suggestion 2

def base_n_to_10(X, n):
    out = 0
    for i in range(len(X)):
        out += int(X[i]) * n ** (len(X) - 1 - i)
    return out

X = input()
M = int(input())

d = 0
for i in range(len(X)):
    d = max(d, int(X[i]))

l = d + 1
r = 10 ** 18 + 1

while r - l > 1:
    m = (r + l) // 2
    if base_n_to_10(X, m) <= M:
        l = m
    else:
        r = m

print(l - d)

=======
Suggestion 3

def solve(x, m):
    d = int(max(x))
    l = d + 1
    r = 10 ** 18 + 1
    while r - l > 1:
        mid = (l + r) // 2
        if check(x, m, mid):
            l = mid
        else:
            r = mid
    return l - (d + 1) + 1

=======
Suggestion 4

def main():
    X = input()
    M = int(input())
    d = max([int(x) for x in X])
    n = d + 1
    while True:
        if int(X, n) > M:
            print(n - d - 1)
            break
        n += 1

=======
Suggestion 5

def base_n(n, x):
    ans = 0
    for i in range(len(x)):
        ans = ans * n + int(x[i])
    return ans

=======
Suggestion 6

def get_num(x, m):
    d = max(x)
    if len(x) == 1:
        if int(x) <= m:
            return 1
        else:
            return 0
    else:
        if int(x[0]) < d:
            return 0
        else:
            return get_num(x[1:], m) + get_num(x[1:], m - int(x[0]))

=======
Suggestion 7

def convert_to_decimal(num_str, radix):
    num = 0
    for i in range(len(num_str)):
        num += int(num_str[-i-1]) * radix ** i
    return num

=======
Suggestion 8

def solve(X,M):
    d = int(max(X)) # X中最大的数字
    if len(X) == 1:
        if int(X) <= M:
            return 1
        else:
            return 0
    # 二分查找
    l = d+1
    r = 10**18+1
    while l < r:
        m = (l+r)//2
        if check(X,M,m):
            l = m + 1
        else:
            r = m
    return l - d - 1

=======
Suggestion 9

def base_n_to_10(x, n):
    out = 0
    for i in x:
        out = out * n + int(i)
    return out

x = input()
m = int(input())

d = max(x)
d = int(d)

ans = 0

=======
Suggestion 10

def solve(x, m):
    d = int(max(x))
    n = int(x, d+1)
    cnt = 0
    while n <= m:
        cnt += 1
        n += 1
    return cnt
