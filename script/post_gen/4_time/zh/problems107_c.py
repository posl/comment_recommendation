Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(n - k + 1):
        l = x[i]
        r = x[i + k - 1]
        if l * r <= 0:
            ans = min(ans, min(-l, r) + r - l)
        else:
            ans = min(ans, max(l, r))
    print(ans)

=======
Suggestion 2

def main():
    print("请输入蜡烛数量和点燃数量：")
    n,k = input().split()
    n = int(n)
    k = int(k)
    print("请输入蜡烛坐标：")
    x = input().split()
    x = list(map(int,x))
    #print(x)
    #print(n,k)
    #print("最小时间为：")
    print(min_time(n,k,x))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        l = X[i]
        r = X[i+K-1]
        ans = min(ans, min(abs(l)+abs(l-r), abs(r)+abs(l-r)))
    print(ans)

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    if k == n:
        print(0)
        return
    elif k == 1:
        print(x[-1] - x[0])
        return
    else:
        ans = 10**9
        for i in range(n-k+1):
            ans = min(ans,x[i+k-1]-x[i]+min(abs(x[i]),abs(x[i+k-1])))
        print(ans)
        return

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    ans = 10**9
    for i in range(n-k+1):
        if x[i]*x[i+k-1] <= 0:
            ans = min(ans, min(abs(x[i]), abs(x[i+k-1]))*2 + max(abs(x[i]), abs(x[i+k-1])))
        else:
            ans = min(ans, max(abs(x[i]), abs(x[i+k-1])))
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))

    #print(N, K)
    #print(x)

    # 从0开始的时间
    time = 0
    # 从0开始向左移动的时间
    time_left = 0
    # 从0开始向右移动的时间
    time_right = 0

    # 将x列表中的正负数分开
    x_left = []
    x_right = []
    for i in x:
        if i < 0:
            x_left.append(i)
        elif i > 0:
            x_right.append(i)
        else:
            pass
    #print(x_left)
    #print(x_right)
    #print(len(x_left))
    #print(len(x_right))

    # 从0开始向左移动的时间
    if len(x_left) > 0:
        time_left = abs(x_left[0])
    # 从0开始向右移动的时间
    if len(x_right) > 0:
        time_right = x_right[-1]

    #print(time_left)
    #print(time_right)

    # 从0开始向左移动的时间和向右移动的时间，取大的值
    time = max(time_left, time_right)

    #print(time)

    # 从0开始的时间，加上从0开始向左移动的时间和向右移动的时间
    time = time + (time_right - time_left)

    #print(time)

    # 从0开始的时间，加上从0开始向左移动的时间和向右移动的时间，再加上点燃蜡烛的时间
    time = time + (x_right[-1] - x_left[0])

    #print(time)

    # 从0开始的时间，加上从0开始向左移动的时间和向右移动的时间，再加上点燃蜡烛的时间，再减去点燃K支蜡烛的时间
    time = time - x_right[-K]

    #print(time)

    # 从0开始的时间，加上从0

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    ans = 10**9
    for i in range(n-k+1):
        if x[i]*x[i+k-1] > 0:
            ans = min(ans,max(abs(x[i]),abs(x[i+k-1])))
        else:
            ans = min(ans,x[i+k-1]-x[i]+min(abs(x[i]),abs(x[i+k-1])))
    print(ans)

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def main():
    n,k = map(int, input().split())
    x = list(map(int, input().split()))
    
    min_time = 10**9
    for i in range(n-k+1):
        if x[i] <= 0 and x[i+k-1] >= 0:
            min_time = min(min_time, abs(x[i])+abs(x[i]-x[i+k-1]), abs(x[i+k-1])+abs(x[i]-x[i+k-1]))
        elif x[i] <= 0 and x[i+k-1] <= 0:
            min_time = min(min_time, abs(x[i]))
        else:
            min_time = min(min_time, abs(x[i+k-1]))
    print(min_time)
