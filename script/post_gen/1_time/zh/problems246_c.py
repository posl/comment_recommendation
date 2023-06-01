Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    res = 0
    for i in range(n):
        if k > 0:
            res += max(a[i] - x, 0)
            k -= 1
        else:
            res += a[i]
    print(res)

=======
Suggestion 2

def resolve():
    n,k,x = map(int,input().split())
    a = list(map(int,input().split()))

    # 优惠券使用策略：优先使用在单价最高的商品上使用优惠券
    # 由于最大单价是10^9，因此优惠券最多只能使用10^9次
    # 优惠券使用次数最多为10^9，因此优惠券最多使用10^9次
    # 优惠券使用次数最多为10^9，因此优惠券最多使用10^9次
    # 优惠券使用次数最多为10^9，因此优惠券最多使用10^9次
    # 优惠券使用次数最多为10^9，因此优惠券最多使用10^9次
    # 优惠券使用次数最多为10^9，因此优惠券最多使用10^9次
    # 优惠券使用次数最多为10^9，因此优惠券最多使用10^9次
    # 优惠券使用次数最多为10^9，因此优惠券最多使用10^9次
    # 优惠券使用次数最多为10^9，因此优惠券最多使用10^9次
    # 优惠券使用次数最多为10^9，因此优惠券最多使用10^9次
    # 优惠券使用次数最多为10^9，因此优惠券最多使用10^9次
    # 优惠券使用次数最多为10^9，因此优惠券最多使用10^9次

    # 优惠券使用策略：优先使用在单价最高的商品上使用优惠券
    # 由于最大单价是10^9，因此优惠

=======
Suggestion 3

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    total = 0
    for i in range(n):
        if k > 0:
            total += max(a[i]-x, 0)
            k -= 1
        else:
            total += a[i]
    print(total)

=======
Suggestion 4

def solve(n, k, x, a):
    cost = 0
    for i in range(n):
        if k > 0:
            cost += max(a[i]-x, 0)
            k -= 1
        else:
            cost += a[i]
    return cost

=======
Suggestion 5

def solve(n, k, x, a):
    sum = 0
    for i in range(n):
        sum += max(a[i] - x, 0)
    return sum

=======
Suggestion 6

def solve():
    N,K,X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if K > 0:
            if A[i] < X:
                ans += A[i]
            else:
                ans += X
            K -= 1
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 7

def problems246_c():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] > k:
            ans += (a[i] - k) * x
            k = 0
        else:
            k -= a[i]
    print(ans)

=======
Suggestion 8

def main():
    # 读入数据
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    # 优惠券数目大于商品数目，直接返回0
    if k >= n:
        print(0)
        return
    # 对商品价格排序
    a.sort()
    # 优惠券最多使用k次，所以最多可以优惠k*x元
    # 如果优惠券最多可以优惠k*x元，那么就优惠掉最贵的k*x元商品
    # 剩下的商品价格之和就是最小价格
    print(sum(a[:n-k]) - k*x)

=======
Suggestion 9

def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if K > 0:
            ans += max(A[i]-X, 0)
            K -= 1
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 10

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if K > 0:
            ans += max(A[i]-X, 0)
            K -= 1
        else:
            ans += A[i]
    print(ans)
