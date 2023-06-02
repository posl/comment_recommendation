Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if k > 0:
            ans += max(a[i] - x, 0)
            k -= 1
        else:
            ans += a[i]
    print(ans)

=======
Suggestion 2

def main():
    n,k,x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if k == 0:
        print(sum(a))
    else:
        print(sum(a[0:n-k]) + k * x)

=======
Suggestion 3

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(N):
        if K > 0:
            count += max(A[i] - X, 0)
            K -= 1
        else:
            count += A[i]
    print(count)

=======
Suggestion 4

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    res = 0
    if k*x > a[-1]:
        res = a[-1]
    else:
        res = k*x
    for i in range(n-1):
        res += a[i]
    print(res)

=======
Suggestion 5

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    result = 0
    for i in range(K):
        if A[i] >= X:
            result += A[i] - X
        else:
            result += 0
    print(result)

=======
Suggestion 6

def get_min_price(n, k, x, a):
    min_price = 0
    for i in range(n):
        if a[i] > x:
            min_price += a[i] - x
        else:
            min_price += 0
    return min_price

=======
Suggestion 7

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum([max(0, i - x) for i in a]))

=======
Suggestion 8

def calc_price(a, k, x):
    return max(a-k*x, 0)

=======
Suggestion 9

def mymain():
    #读取输入
    n,k,x = map(int,input().split())
    a = list(map(int,input().split()))
    #计算
    ans = 0
    for i in range(n):
        if i%2 == 0:
            ans += max(a[i]-x,0)
        else:
            ans += a[i]
    #输出
    print(ans)

mymain()

=======
Suggestion 10

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(n):
        if k > 0:
            if a[i] > x:
                ans += a[i] - x
                k -= 1
            else:
                ans += a[i]
        else:
            ans += a[i]
    print(ans)
