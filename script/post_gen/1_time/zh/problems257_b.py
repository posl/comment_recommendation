Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    #初始化棋子位置
    x = [0] * n
    for i in range(k):
        x[a[i] - 1] = 1
    #执行棋子操作
    for i in range(q):
        for j in range(n - 1):
            if l[i] == j + 1 and x[j] == 1 and x[j + 1] == 0:
                x[j] = 0
                x[j + 1] = 1
    #输出棋子位置
    for i in range(n):
        if x[i] == 1:
            print(i + 1, end=" ")
    print()

=======
Suggestion 2

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    # print(N, K, Q)
    # print(A)
    # print(L)
    # print(len(L))
    # print(len(A))

    # 棋子的位置
    chess = [0 for i in range(N)]
    for i in range(K):
        chess[A[i]-1] = 1
    # print(chess)

    # 棋子移动
    for i in range(Q):
        # print(L[i])
        # print(chess)
        # print(chess[L[i]-1])
        if chess[L[i]-1] == 1:
            continue
        else:
            # print(chess)
            # print(L[i])
            # print(L[i]-1)
            # print(chess[L[i]-1])
            # print(chess[L[i]])
            if chess[L[i]] == 0:
                chess[L[i]-1] = 0
                chess[L[i]] = 1
            else:
                continue
            # print(chess)

    # print(chess)

    # 输出棋子位置
    for i in range(N):
        if chess[i] == 1:
            print(i+1, end=' ')
    print('')

=======
Suggestion 3

def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    ans = [0] * (n+1)
    for i in range(k):
        ans[a[i]] += 1
    for i in range(n):
        ans[i+1] += ans[i]
    for i in range(q):
        print(ans[l[i]] - ans[l[i]-1])

=======
Suggestion 4

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    for i in range(q):
        if a[l[i]-1] == n:
            continue
        elif a[l[i]-1] < n:
            if a[l[i]-1] + 1 in a:
                continue
            else:
                a[l[i]-1] += 1
    for i in range(k):
        print(a[i], end=' ')

=======
Suggestion 5

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    #print(N, K, Q)
    #print(A)
    #print(L)
    #print()
    
    #棋子初始位置
    chess_list = [0]*N
    for i in range(K):
        chess_list[A[i]-1] = 1
    #print(chess_list)
    
    #棋子移动
    for i in range(Q):
        for j in range(L[i]-1, N-1):
            if chess_list[j] == 1 and chess_list[j+1] == 0:
                chess_list[j], chess_list[j+1] = 0, 1
    #print(chess_list)
    
    #打印棋子位置
    for i in range(K):
        for j in range(N):
            if chess_list[j] == 1:
                print(j+1, end=' ')
    print()

=======
Suggestion 6

def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))

    #棋子的位置
    pos = [0] * n
    for i in range(k):
        pos[a[i]-1] += 1
    for i in range(n-1,0,-1):
        pos[i-1] += pos[i]
    for i in range(q):
        print(pos[l[i]-1])

=======
Suggestion 7

def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))

    #初始化
    #l中的值对应a中的索引
    #r中的值对应a中的值
    r = [0]*n
    for i in range(k):
        r[a[i]-1] = 1

    #计算每个位置的值
    for i in range(n):
        if r[i] == 0:
            r[i] = r[i-1]

    #计算每个位置的值
    for i in range(q):
        print(r[l[i]-1])

=======
Suggestion 8

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    result = [0] * K
    for i in range(K):
        result[i] = A[L[i] - 1]
    for i in range(Q):
        if result.count(result[i]) > 1:
            continue
        else:
            for j in range(i + 1, Q):
                if result[i] == result[j]:
                    result[j] = result[i]
    result.sort()
    print(*result)

=======
Suggestion 9

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))

    # 移动棋子
    for i in range(q):
        for j in range(k):
            if l[j] < k and a[l[j]] < a[l[j] + 1]:
                a[l[j]] += 1

    # 打印结果
    for i in range(k):
        print(a[i], end=' ')

=======
Suggestion 10

def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    #print(n,k,q)
    #print(a)
    #print(l)
    #print(l[0])
    #print(a[l[0]-1])
    #print(a[l[0]-1]+1)
    #print(a[l[0]-1]+1<=n)
    #print(a[l[0]-1]+1 not in a)
    #print(a[l[0]-1]+1 not in a)
    #print('----')
    #print(a)
    #print(l)
    #print('----')
    for i in range(q):
        if a[l[i]-1]+1<=n and a[l[i]-1]+1 not in a:
            a[l[i]-1] += 1
    for i in range(k):
        print(a[i],end=' ')
