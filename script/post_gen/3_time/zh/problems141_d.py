Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(m):
        a[i] = a[i] // 2
    a.sort(reverse=True)
    print(sum(a[m:]))
    return

=======
Suggestion 3

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(m):
        a[i] = a[i] // 2
    a.sort(reverse=True)
    print(sum(a))

=======
Suggestion 4

def buy_goods(n, m, a):
    a.sort(reverse=True)
    for i in range(m):
        a[0] = a[0] // 2
        a.sort(reverse=True)
    return sum(a)

=======
Suggestion 5

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for _ in range(m):
        a.append(a.pop()//2)
    print(sum(a))

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(m):
        a[n - 1] = a[n - 1] // 2
        a.sort()
    print(sum(a))

=======
Suggestion 7

def solve(n, m, a):
    # 简单的贪心算法
    # 由于 2^30 > 10^9，所以最多只能使用30张门票
    # 从最低价的商品开始购买，使用尽可能多的门票
    # 如果使用了i张门票，那么购买该商品的价格为 a[i] / (2^i)
    # 由于 a[i] 是整数，所以 a[i] / (2^i) = a[i] >> i
    # 由于 a[i] 最大是10^9，所以 a[i] >> i 最大是 10^9 / (2^30) = 0
    # 所以最多只需要30张门票
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] >> i
    return ans

=======
Suggestion 8

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(m):
        a[-1] = a[-1]//2
        a.sort()
    print(sum(a))

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(m):
        a[-1] = a[-1]//2
        a.sort()
    print(sum(a))
