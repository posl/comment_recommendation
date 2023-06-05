Synthesizing 10/10 solutions

=======
Suggestion 1

def func(h,w,k):
    #h,w,k=map(int,input().split())
    #h,w,k=1,3,2
    #h,w,k=1,3,1
    #h,w,k=2,3,3
    #h,w,k=2,3,1
    #h,w,k=7,1,1
    #h,w,k=15,8,5
    if k==1:
        if h==1:
            return 1
        else:
            return 2**(h-2)
    elif k==w:
        if h==1:
            return 1
        else:
            return 2**(h-2)
    else:
        if h==1:
            return 1
        else:
            return 2**(h-3)
    #print(h,w,k)
    #print(2**(h-2))
    #print(2**(h-3))
    #print(2**(h-2)+2**(h-3))
    #print(2**(h-2)+2**(h-3)-2)
    #print(2**(h-2)+2**(h-3)-2-2**(h-3))
    #print(2**(h-2)+2**(h-3)-2-2**(h-3)-2**(h-3))
    #print(2**(h-2)+2**(h-3)-2-2**(h-3)-2**(h-3)-2**(h-3))
    #print(2**(h-2)+2**(h-3)-2-2**(h-3)-2**(h-3)-2**(h-3)-2**(h-3))
    #print(2**(h-2)+2**(h-3)-2-2**(h-3)-2**(h-3)-2**(h-3)-2**(h-3)-2**(h-3))

=======
Suggestion 2

def amidakuji(H,W,K):
    if H==1:
        return 1
    if K==1:
        return 2**(W-1)
    if K==W:
        return 2**(W-1)
    return amidakuji(H-1,W-1,K-1)+amidakuji(H-1,W,K-1)

=======
Suggestion 3

def amidakuji(H,W,K):
    #H:垂直线的长度
    #W:垂直线的数量
    #K:最左边的垂直线的顶部追踪到底部，当我们遇到水平线时，我们会从左边到达第K条垂直线的底部。
    #返回满足条件的羊皮纸的数量
    #如果我们从最左边的垂直线的顶部追踪到底部，当我们遇到水平线时，我们会从左边到达第K条垂直线的底部。
    #垂直线的数量为W，从最左边的垂直线的顶部追踪到底部，当我们遇到水平线时，我们会从左边到达第K条垂直线的底部。
    #如果我们从最左边的垂直线的顶部追踪到底部，当我们遇到水平线时，我们会从左边到达第K条垂直线的底部。
    #垂直线的数量为W，从最左边的垂直线的顶部追踪到底部，当我们遇到水平线时，我们会从左边到达第K条垂直线的底部。
    #如果我们从最左边的垂直线的顶部追踪到底部，当我们遇到水平线时，我们会从左边到达第K条垂直线的底部。
    #垂直线的数量为W，从最左边的垂直线的顶部追踪到底部，当我们遇到水平线时，我们会从左边到达第K条垂直线的底部。
    #如果我们从最左

=======
Suggestion 4

def get_matrix(H,W):
    matrix = []
    for i in range(H+1):
        matrix.append([])
        for j in range(W):
            matrix[i].append(0)
    return matrix

=======
Suggestion 5

def main():
    h,w,k = map(int, input().split())
    if w == 1:
        print(1)
        return
    dp = [[0 for i in range(w)] for j in range(h+1)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if j == 0:
                dp[i+1][j] = (dp[i][j] * (2**(w-2))) % 1000000007
            elif j == w-1:
                dp[i+1][j] = (dp[i][j] * (2**(w-2))) % 1000000007
            else:
                dp[i+1][j] = (dp[i][j-1] * (2**(w-j-2)) * dp[i][j] * (2**(j-1))) % 1000000007
    print(dp[h][k-1])

=======
Suggestion 6

def func(h,w,k):
    if w == 1:
        if k == 1:
            return 1
        else:
            return 0
    else:
        if k == 1:
            return func(h,w-1,1) + func(h,w-1,2)
        elif k == w:
            return func(h,w-1,w-1) + func(h,w-1,w)
        else:
            return func(h,w-1,k-1) + func(h,w-1,k) + func(h,w-1,k+1)

=======
Suggestion 7

def amidakuji(H, W, K):
    if W == 1:
        return 1

    dp = [[0 for _ in range(W)] for _ in range(H + 1)]
    dp[0][0] = 1
    for i in range(1, H + 1):
        for j in range(W):
            if j == 0:
                dp[i][j] = dp[i - 1][j + 1]
            elif j == W - 1:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
            dp[i][j] %= 1000000007

    return dp[H][K - 1]

=======
Suggestion 8

def calculate(h,w,k):
    if k == 1:
        return 1
    if k == w:
        return 1
    if k == w-1:
        return w-1
    if k == 2:
        return w
    if k == w-2:
        return w*(w-1)/2
    if k == 3:
        return w*(w-1)/2
    if k == w-3:
        return w*(w-1)*(w-2)/6
    if k == 4:
        return w*(w-1)*(w-2)/6
    if k == w-4:
        return w*(w-1)*(w-2)*(w-3)/24
    if k == 5:
        return w*(w-1)*(w-2)*(w-3)/24
    if k == w-5:
        return w*(w-1)*(w-2)*(w-3)*(w-4)/120
    if k == 6:
        return w*(w-1)*(w-2)*(w-3)*(w-4)/120
    if k == w-6:
        return w*(w-1)*(w-2)*(w-3)*(w-4)*(w-5)/720
    if k == 7:
        return w*(w-1)*(w-2)*(w-3)*(w-4)*(w-5)/720
    if k == w-7:
        return w*(w-1)*(w-2)*(w-3)*(w-4)*(w-5)*(w-6)/5040
    if k == 8:
        return w*(w-1)*(w-2)*(w-3)*(w-4)*(w-5)*(w-6)/5040
    if k == w-8:
        return w*(w-1)*(w-2)*(w-3)*(w-4)*(w-5)*(w-6)*(w-7)/40320
    if k == 9:
        return w*(w-1)*(w-2)*(w-3)*(w-4)*(w-5)*(w-6)*(w-7)/40320
    if k == w-9:
        return w*(w-1)*(w-2)*(w-3)*(w-4)*(w-

=======
Suggestion 9

def f(h,w,k):
    if h==1:
        if k==1:
            return w
        else:
            return 0
    else:
        if k==1:
            return f(h-1,w,k)+f(h-1,w,k+1)
        elif k==w:
            return f(h-1,w,k-1)+f(h-1,w,k)
        else:
            return f(h-1,w,k-1)+f(h-1,w,k)+f(h-1,w,k+1)
h,w,k=map(int,input().split())
print(f(h,w,k)%1000000007)

=======
Suggestion 10

def amidakuji(H, W, K):
    if H == 1:
        return 1
    if K == 1:
        return amidakuji(H-1, W, K) + amidakuji(H-1, W, K+1)
    if K == W:
        return amidakuji(H-1, W, K-1) + amidakuji(H-1, W, K)
    return amidakuji(H-1, W, K-1) + amidakuji(H-1, W, K) + amidakuji(H-1, W, K+1)
