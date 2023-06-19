Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    pass

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    t = K // N
    K = K % N
    for i in range(N):
        if a[i] <= t:
            a[i] = 1
        else:
            a[i] = 0
    for i in range(N):
        if K > 0 and a[i] == 0:
            a[i] = 1
            K -= 1
    for i in range(N):
        print(a[i])
main()

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    t = k//n
    r = k%n
    for i in range(n):
        if i < r:
            print(t+1)
        else:
            print(t)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    d = k // n
    r = k % n
    for i in range(n):
        print(d + (1 if i < r else 0))

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(range(n))
    b.sort(key=lambda i: a[i])
    c = [0] * n
    for i in range(n):
        c[b[i]] = k // n
        if i < k % n:
            c[b[i]] += 1
    for i in range(n):
        print(c[i])

=======
Suggestion 6

def main():
    # 读入数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 对数据进行排序
    a.sort()
    # 求出每人分得的糖果
    # 每人分得的糖果的最小值
    min_candy = k // n
    # 余下的糖果
    remain_candy = k % n
    # 分配糖果
    for i in range(n):
        # 当前分配的糖果数
        candy = min_candy
        if remain_candy > 0:
            candy += 1
            remain_candy -= 1
        # 输出结果
        print(candy)

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    print(a)
    b = [0]*N
    for i in range(N):
        if i == 0:
            b[i] = a[i]
        else:
            b[i] = a[i] - a[i-1]
    print(b)
    for i in range(N):
        if i == 0:
            b[i] = b[i]
        else:
            b[i] = b[i-1] + b[i]
    print(b)
    for i in range(N):
        if i == 0:
            b[i] = b[i]
        else:
            b[i] = b[i-1] + b[i]
    print(b)
    for i in range(N):
        if i == 0:
            b[i] = b[i]
        else:
            b[i] = b[i-1] + b[i]
    print(b)
    for i in range(N):
        if i == 0:
            b[i] = b[i]
        else:
            b[i] = b[i-1] + b[i]
    print(b)
    for i in range(N):
        if i == 0:
            b[i] = b[i]
        else:
            b[i] = b[i-1] + b[i]
    print(b)
    for i in range(N):
        if i == 0:
            b[i] = b[i]
        else:
            b[i] = b[i-1] + b[i]
    print(b)
    for i in range(N):
        if i == 0:
            b[i] = b[i]
        else:
            b[i] = b[i-1] + b[i]
    print(b)
    for i in range(N):
        if i == 0:
            b[i] = b[i]
        else:
            b[i] = b[i-1] + b[i]
    print(b)

    for i in range(N):
        if K >= b[i]:
            print(a[i])
        else:
            print(a[i] - (b[i] - K))
            break

=======
Suggestion 8

def solution1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(a)
    if k >= n:
        for i in range(n):
            print(k//n)
    else:
        for i in range(n):
            if a[i] == a[0]:
                print(k//n + 1)
            else:
                print(k//n)

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    #print(a)
    #print(n,k)
    #print(a)
    #print(a[0])
    #print(a[n-1])
    #print(k//n)
    #print(k%n)
    for i in range(n):
        print(k//n+1 if a[i] <= k%n else k//n)

=======
Suggestion 10

def main():
    pass
