Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    count = 0
    for i in range(n):
        if k > 0:
            count += min(a[i],x)
            k -= 1
        else:
            count += a[i]
    print(count)

=======
Suggestion 2

def solve():
    n,k,x = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in range(n):
        if k > 0:
            ans += max(A[i]-x,0)
            k -= 1
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 3

def main():
    #n,k,x = map(int,input().split())
    n,k,x = 5,4,7
    #a = list(map(int,input().split()))
    a = [8,3,10,5,13]
    a.sort()
    #print(a)
    ans = 0
    for i in range(n):
        if k > 0:
            ans += max(a[i]-x,0)
            #print(ans)
            k -= 1
        else:
            ans += a[i]
            #print(ans)
    print(ans)

=======
Suggestion 4

def price(a, k, x):
    return max(a-k*x, 0)

=======
Suggestion 5

def get_min_cost(num, coupon_num, coupon_price, price_list):
    cost = 0
    for price in price_list:
        if coupon_num > 0:
            cost += max(price - coupon_price, 0)
            coupon_num -= 1
        else:
            cost += price
    return cost

=======
Suggestion 6

def main():
    #N,K,X = map(int,input().split())
    #A = list(map(int,input().split()))
    #print(N,K,X)
    #print(A)
    N,K,X = 20,815,60
    A = [2066, 3193, 2325, 4030, 3725, 1669, 1969, 763, 1653, 159, 5311, 5341, 4671, 2374, 4513, 285, 810, 742, 2981, 202]
    A.sort()
    sum = 0
    for i in range(N):
        if K>0:
            if A[i]>=X:
                sum += A[i]-X
                K -= 1
            else:
                sum += A[i]
        else:
            sum += A[i]
    print(sum)

=======
Suggestion 7

def solve():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if k > 0:
            ans += max(a[i]-x, 0)
            k -= 1
        else:
            ans += a[i]
    return ans

print(solve())

=======
Suggestion 8

def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        if A[i] >= X:
            ans += A[i] - X
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 9

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if k >= n:
        print(0)
        return
    if k == 1:
        print(a[0])
        return
    if k == 2:
        print(a[1])
        return
    if k == 3:
        print(a[1]+a[0])
        return
    if k == 4:
        print(a[2]+a[1])
        return
    if k == 5:
        print(a[2]+a[1]+a[0])
        return
    if k == 6:
        print(a[3]+a[2])
        return
    if k == 7:
        print(a[3]+a[2]+a[1])
        return
    if k == 8:
        print(a[3]+a[2]+a[1]+a[0])
        return
    if k == 9:
        print(a[4]+a[3])
        return
    if k == 10:
        print(a[4]+a[3]+a[2])
        return
    if k == 11:
        print(a[4]+a[3]+a[2]+a[1])
        return
    if k == 12:
        print(a[4]+a[3]+a[2]+a[1]+a[0])
        return
    if k == 13:
        print(a[5]+a[4])
        return
    if k == 14:
        print(a[5]+a[4]+a[3])
        return
    if k == 15:
        print(a[5]+a[4]+a[3]+a[2])
        return
    if k == 16:
        print(a[5]+a[4]+a[3]+a[2]+a[1])
        return
    if k == 17:
        print(a[5]+a[4]+a[3]+a[2]+a[1]+a[0])
        return
    if k == 18:
        print(a[6]+a[5])
        return
    if k == 19:
        print(a[6]+a[5]+a[4])
        return

=======
Suggestion 10

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    cost = 0

    for i in range(n):
        if k > 0:
            if a[i] < x:
                cost += a[i]
                k -= 1
            else:
                cost += x
        else:
            cost += a[i]

    print(cost)
