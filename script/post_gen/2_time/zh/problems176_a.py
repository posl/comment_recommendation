Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    return

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -float('inf')
    for i in range(n):
        x = i
        s = 0
        t = 0
        while True:
            x = p[x] - 1
            s += c[x]
            t += 1
            if x == i:
                break
            if t == k:
                break
        if c[x] > 0:
            u = (k // t - 1) * s
        else:
            u = 0
        for j in range(k % t):
            x = p[x] - 1
            u += c[x]
            ans = max(ans, u)
    print(ans)

=======
Suggestion 4

def main():
    #读入数据
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    #print(n, k, p, c)
    #print(len(p), len(c))
    
    #定义最大分数
    max_score = -10**9 - 1
    
    #遍历所有可能的起点
    for i in range(n):
        #print('i =', i)
        #定义当前分数
        current_score = 0
        #定义当前位置
        current_position = i
        #定义当前步数
        current_step = 0
        #定义当前最大分数
        current_max_score = -10**9 - 1
        #定义当前循环的步数
        current_loop_step = 0
        #定义当前循环的最大分数
        current_loop_max_score = -10**9 - 1
        
        #如果k大于n，则可以循环k//n次，再加上k%n次
        if k >= n:
            #print('k >= n')
            #print('k // n =', k // n)
            #print('k % n =', k % n)
            #遍历k//n次
            for j in range(k // n):
                #print('j =', j)
                #print('current_step =', current_step)
                #print('current_position =', current_position)
                #print('current_score =', current_score)
                #print('current_max_score =', current_max_score)
                
                #如果当前位置和当前步数的最大分数大于当前循环的最大分数，则更新当前循环的最大分数
                if c[p[current_position] - 1] + current_score > current_loop_max_score:
                    current_loop_max_score = c[p[current_position] - 1] + current_score
                
                #更新当前位置
                current_position = p[current_position] - 1
                #更新当前步数
                current_step += 1
                #更新当前分数
                current_score += c[current_position]
                
                #如果当前位置和当前步数的最大分数大于当前最

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ans = -10 ** 18
    for i in range(N):
        # 一圈的得分
        score = 0
        # 一圈的步数
        cnt = 0
        # 一圈的开始位置
        j = i
        while True:
            # 走一步
            j = P[j] - 1
            score += C[j]
            cnt += 1
            # 一圈走完了
            if j == i:
                break
        # 一圈的得分
        loop = score
        # 一圈的步数
        loop_cnt = cnt
        # 一圈的开始位置
        loop_start = i
        # 一圈的得分
        score = 0
        # 一圈的步数
        cnt = 0
        # 一圈的开始位置
        j = i
        while True:
            # 走一步
            j = P[j] - 1
            score += C[j]
            cnt += 1
            # 一圈走完了
            if j == i:
                break

        # 一圈的得分
        loop = score
        # 一圈的步数
        loop_cnt = cnt
        # 一圈的开始位置
        loop_start = i

        # 一圈的得分
        score = 0
        # 一圈的步数
        cnt = 0
        # 一圈的开始位置
        j = i
        while True:
            # 走一步
            j = P[j] - 1
            score += C[j]
            cnt += 1
            # 一圈走完了
            if j == i:
                break
        # 一圈的得分
        loop = score
        # 一圈的步数
        loop_cnt = cnt
        # 一圈的开始位置
        loop_start = i

        # 一

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10**18
    for i in range(n):
        x = i
        s = 0
        t = 0
        while True:
            x = p[x] - 1
            s += c[x]
            t += 1
            if x == i:
                break
            if t == k:
                break
        if c[x] > 0:
            u = (k // t - 1) * s
            ans = max(ans, u)
            for j in range(k % t):
                x = p[x] - 1
                u += c[x]
                ans = max(ans, u)
        else:
            ans = max(ans, s)
    print(ans)
    return

main()

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    c = list(map(int,input().split()))
    p = [p[i]-1 for i in range(n)]
    ans = -float("inf")
    for i in range(n):
        now = i
        tmp = 0
        cnt = 0
        while True:
            cnt += 1
            tmp += c[p[now]]
            now = p[now]
            ans = max(ans,tmp)
            if cnt == k:
                break
            if now == i:
                break
    print(ans)

=======
Suggestion 8

def solve(n, k, p, c):
    # 从1号格开始，走一步就把棋子送到2号格，之后的分数是4。
    # 如果我们从方格2开始，走一步棋将棋子送到方格4，之后的分数是-8。再走一步棋将棋子送到方格1，之后的分数是-8+3=-5。
    # 如果我们从3号方格开始，走一步棋将棋子送到5号方格，之后的分数是8。再走一步棋将棋子送到3号方格，之后的分数是8+（-10）=-2。
    # 如果我们从方格4开始，走一步棋将棋子送到方格1，之后的分数是3。再走一步棋将棋子送到方格2，之后的分数是3+4=7。
    # 如果我们从5号方格开始，走一步棋会把棋子送到3号方格，之后的分数是-10。再走一步就把棋子送到5号方格，之后的分数是-10+8=-2。
    # 最高得分是8分。
    # 1.从1号格开始，走一步就把棋子送到2号格，之后的分数是4。
    # 2.如果我们从方格2开始，走一步棋将棋子送到方格4，之后的分数是-8。再走一步棋将棋子送到方格1，之后的分数是-8+3=-5。
    # 3.如果我们从3号方格开始，走一步棋将棋子送到5号方格，之后的分数是8。再走一步棋将棋子送到3号方格，之后的分数是8+（-10）=-2。
    # 4.如果
