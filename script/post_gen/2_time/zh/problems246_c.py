Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k, x = map(int, input().split())
    items = list(map(int, input().split()))
    items.sort()
    total = 0
    for item in items[:-k]:
        total += item
    total += k * x
    print(total)

=======
Suggestion 2

def main():
    n, k, x = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(n):
        if k > 0:
            ans += max(A[i]-x, 0)
            k -= 1
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 3

def cal_min(x, k, a):
    if x > a:
        return 0
    return a - k * x

=======
Suggestion 4

def solve(N, K, X, A):
    ans = 0
    for i in range(N):
        ans += max(A[i]-X, 0)
    return ans

=======
Suggestion 5

def solution(n, k, x, a):
    sum = 0
    for i in range(n):
        sum += max(a[i]-x, 0)
    return sum

=======
Suggestion 6

def main():
    n,k,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    print(sum(a[:n-k])+x*(k-1))

=======
Suggestion 7

def get_min_price(n, k, x, a):
    a.sort()
    price = 0
    for i in range(n):
        if k > 0:
            if a[i] < x:
                price += a[i]
            else:
                price += x
            k -= 1
        else:
            price += a[i]
    return price

=======
Suggestion 8

def main():
    N,K,X = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if K > 0:
            if A[i] > X:
                ans += A[i] - X
                K -= 1
            else:
                ans += A[i]
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 9

def buy(n, k, x, a):
    cost = 0
    for i in range(n):
        if a[i] > x:
            cost += a[i] - x
    cost = min(cost, k)
    return cost

=======
Suggestion 10

def get_min_price(n, k, x, a):
    # 优惠券数大于等于商品数，返回0
    if k >= n:
        return 0
    # 优惠券数小于商品数，返回最小价格
    else:
        # 将商品价格从低到高排序
        a.sort()
        # 优惠券数
        coupon_num = k
        # 优惠券可以用的商品数
        coupon_product_num = k * x
        # 优惠券可以用的商品数大于等于商品数，返回0
        if coupon_product_num >= n:
            return 0
        # 优惠券可以用的商品数小于商品数，返回最小价格
        else:
            # 优惠券可以用的商品数小于商品数，返回最小价格
            # 优惠券不足以买所有商品，返回最小价格
            else:
                # 优惠券可以用的商品数小于商品数，返回最小价格
                # 优惠券不足以买所有商品，返回最小价格
                else:
                    # 优惠券可以用的商品数小于商品数，返回最小价格
                    # 优惠券不足以买所有商品，返回最小价格
                    else:
                        # 优惠券可以用的商品数小于商品数，返回最小价格
                        # 优惠券不足以买所有商品，返回最小价格
                        else:
                            # 优惠券可以用的商品数小于商品数，返回最小价格
                            # 优惠券不足以买所有商品，返回最小价格
                            else:
                                # 优惠券可以用的商品数小于商品数，返回最小价格
                                # 优惠券不足以买所有商品，返回最小价格
                                else:
                                    # 优惠券可以用的商品数小于商品数，返回最小价格
                                    # 优惠券
