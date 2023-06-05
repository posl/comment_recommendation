Synthesizing 10/10 solutions

=======
Suggestion 1

def problems159_d():
    return None

=======
Suggestion 2

def get_sum(n, k):
    return int(n * (n - 1) / 2)

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 1
        else:
            d[a[i]] += 1
    ans = 0
    for i in d.values():
        ans += i * (i - 1) // 2
    for i in range(n):
        print(ans - d[a[i]] + 1)

=======
Suggestion 5

def solve(n, a):
    # 从N-1个球中选择两个不同的球（不考虑顺序），而不是第k个球，以使写在它们上面的整数相等的方法的数量。
    # 从N-1个球中选择两个不同的球（不考虑顺序），而不是第k个球，以使写在它们上面的整数相等的方法的数量。
    # 从N-1个球中选择两个不同的球（不考虑顺序），而不是第k个球，以使写在它们上面的整数相等的方法的数量。
    # 从N-1个球中选择两个不同的球（不考虑顺序），而不是第k个球，以使写在它们上面的整数相等的方法的数量。
    # 从N-1个球中选择两个不同的球（不考虑顺序），而不是第k个球，以使写在它们上面的整数相等的方法的数量。
    # 从N-1个球中选择两个不同的球（不考虑顺序），而不是第k个球，以使写在它们上面的整数相等的方法的数量。
    # 从N-1个球中选择两个不同的球（不考虑顺序），而不是第k个球，以使写在它们上面的整数相等的方法的数量。
    # 从N-1个球中选择两个不同的球（不考虑顺序），而不是第k个球，以使写在它们上面的整数相等的方法的数量。
    # 从N-1个球中选择两个不同的球（不考虑顺序），而不是第k个球，以使写在它们上面的整数相等的方法的数量。

    # 从N-1个球中选择两个不同的球（

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0]*N
    for i in range(N):
        ans[i] = A.count(A[i])
    for i in range(N):
        print(ans[i]-1)

solve()

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n + 1)
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    for i in range(1, n + 1):
        ans += b[i] * (b[i] - 1) // 2
    for i in range(n):
        print(ans - b[a[i]] + 1)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n + 1)
    for i in a:
        b[i] += 1
    ans = 0
    for i in range(1, n + 1):
        ans += b[i] * (b[i] - 1) // 2
    for i in a:
        print(ans - (b[i] - 1))

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    num = {}
    for i in range(n):
        if a[i] not in num:
            num[a[i]] = 1
        else:
            num[a[i]] += 1
    total = 0
    for i in num:
        total += num[i] * (num[i] - 1) // 2
    for i in range(n):
        print(total - num[a[i]] + 1)

=======
Suggestion 10

def solve(n, a):
    c = [0] * (n + 1)
    for i in range(n):
        c[a[i]] += 1
    ans = 0
    for i in range(n):
        ans += c[i] * (c[i] - 1) // 2
    for i in range(n):
        print(ans - c[a[i]] + 1)

n = int(input())
a = list(map(int, input().split()))
solve(n, a)
