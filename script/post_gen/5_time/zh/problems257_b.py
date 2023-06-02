Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    B = [0] * N
    for i in range(K):
        B[A[i]-1] += 1
    for i in range(N):
        if B[i] > 0:
            B[i] = 1
    for i in range(Q):
        if B[L[i]-1] == 1:
            B[L[i]-1] = 0
            if L[i] < N:
                B[L[i]] = 1
        else:
            B[L[i]-1] = 1
    for i in range(N):
        if B[i] == 1:
            print(i+1, end=' ')
    print()

=======
Suggestion 2

def main():
    #n = 5
    #k = 3
    #q = 5
    #a = [1, 3, 4]
    #l = [3, 3, 1, 1, 2]
    #n = 2
    #k = 2
    #q = 2
    #a = [1, 2]
    #l = [1, 2]
    #n = 10
    #k = 6
    #q = 9
    #a = [1, 3, 5, 7, 8, 9]
    #l = [1, 2, 3, 4, 5, 6, 5, 6, 2]
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    #print(n, k, q)
    #print(a)
    #print(l)
    #print(len(a))
    #print(len(l))
    #print(a[1])
    #print(l[1])
    #print(a[2])
    #print(l[2])
    #print(a[3])
    #print(l[3])
    #print(a[4])
    #print(l[4])
    #print(a[5])
    #print(l[5])
    #print(a[6])
    #print(l[6])
    #print(a[7])
    #print(l[7])
    #print(a[8])
    #print(l[8])
    #print(a[9])
    #print(l[9])
    #print(a[10])
    #print(l[10])
    #print(a[11])
    #print(l[11])
    #print(a[12])
    #print(l[12])
    #print(a[13])
    #print(l[13])
    #print(a[14])
    #print(l[14])
    #print(a[15])
    #print(l[15])
    #print(a[16])
    #print(l[16])
    #print(a[17])
    #print(l[17])
    #print(a[18])
    #print(l[18])
    #print(a[19])
    #print(l

=======
Suggestion 3

def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    s = []
    for i in range(n):
        s.append(0)
    for i in range(k):
        s[a[i]-1] += 1
    for i in range(q):
        for j in range(k):
            if s[l[j]-1] == 1 and l[j] != n:
                s[l[j]-1] -= 1
                s[l[j]] += 1
            elif s[l[j]-1] == 1 and l[j] == n:
                s[l[j]-1] -= 1
            else:
                continue
    for i in range(n):
        if s[i] == 1:
            print(i+1,end=' ')
        else:
            continue

=======
Suggestion 4

def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    ans = []
    for i in range(n):
        ans.append(0)
    for i in range(k):
        ans[a[i]-1] += 1
    for i in range(n):
        ans[i] = q-ans[i]
    for i in range(q):
        ans[l[i]-1] += 1
    for i in range(n):
        if ans[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    ans = [0] * n
    for i in range(k):
        ans[a[i] - 1] += 1
    for i in range(n - 1):
        ans[i + 1] += ans[i]
    for i in range(q):
        print(ans[l[i] - 1])

=======
Suggestion 6

def main():
    n,k,q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))

    #print(n,k,q)
    #print(a)
    #print(l)

    #初始化
    #棋子位置
    chess = [0] * n
    for i in a:
        chess[i-1] = 1
    #print(chess)

    #操作
    for i in l:
        #print(i)
        #print(chess)
        if chess[i-1] == 1:
            #print("ok")
            continue
        else:
            #print("no")
            for j in range(i,n):
                #print(j)
                if chess[j] == 0:
                    chess[j] = 1
                    break
            #print(chess)

    #print(chess)
    #打印结果
    for i in range(n):
        if chess[i] == 1:
            print(i+1, end=" ")

=======
Suggestion 7

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    for i in range(1, Q + 1):
        if A[L[i - 1] - 1] < N and (A[L[i - 1] - 1] + 1) not in A:
            A[L[i - 1] - 1] += 1
    for i in range(K):
        print(A[i], end=" ")
    print()

=======
Suggestion 8

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))

    # print(N, K, Q, A, L)

    # 生成棋盘
    board = [0] * N
    for i in A:
        board[i - 1] = 1

    # print(board)

    # 棋子移动
    for i in L:
        if board[i - 1] == 1:
            continue
        else:
            # 棋子移动
            for j in range(i - 1, N):
                if board[j] == 0:
                    board[j] = 1
                    break

    # print(board)

    # 输出
    for i in range(K):
        for j in range(N):
            if board[j] == 1:
                print(j + 1, end=' ')
                board[j] = 0
                break

=======
Suggestion 9

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    ans = [0] * N
    for i in range(K):
        ans[A[i]-1] = 1
    for i in range(Q):
        for j in range(K):
            if ans[A[L[j]-1]-1] == 1 and A[L[j]-1] != N:
                ans[A[L[j]-1]-1] = 0
                ans[A[L[j]-1]] = 1
                A[L[j]-1] += 1
    for i in range(N):
        if ans[i] == 1:
            print(i+1, end=" ")
    print()
