Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    b = [0] * n
    for i in range(k):
        b[a[i] - 1] += 1
    for i in range(q):
        for j in range(k):
            if b[a[l[j] - 1] - 1] == 0:
                a[l[j] - 1] += 1
                b[a[l[j] - 1] - 1] += 1
    print(' '.join(map(str, a)))

=======
Suggestion 2

def main():
    N,K,Q = map(int,input().split())
    A = list(map(int,input().split()))
    L = list(map(int,input().split()))
    #print(N,K,Q)
    #print(A)
    #print(L)
    #N,K,Q = 5,3,5
    #A = [1,3,4]
    #L = [3,3,1,1,2]
    #N,K,Q = 2,2,2
    #A = [1,2]
    #L = [1,2]
    #N,K,Q = 10,6,9
    #A = [1,3,5,7,8,9]
    #L = [1,2,3,4,5,6,5,6,2]
    #print(N,K,Q)
    #print(A)
    #print(L)

    #棋子的位置
    p = [0]*N
    for i in range(K):
        p[A[i]-1] += 1
    #print(p)

    #棋子移动
    for i in range(Q):
        for j in range(K):
            if p[L[j]-1] == N:
                continue
            elif p[L[j]] == 0:
                p[L[j]-1] -= 1
                p[L[j]] += 1
    #print(p)

    #输出
    for i in range(K):
        print(p[i],end=' ')
    print()

=======
Suggestion 3

def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    for i in range(q):
        if a[l[i]-1] < a[l[i]]:
            a[l[i]-1],a[l[i]] = a[l[i]],a[l[i]-1]
    for i in range(k):
        print(a[i],end=' ')

main()

=======
Suggestion 4

def main():
    N,K,Q=map(int,input().split())
    A=list(map(int,input().split()))
    L=list(map(int,input().split()))
    #print(N,K,Q,A,L)
    #初始化
    #空间复杂度O(N)
    #时间复杂度O(N)
    #B=[0]*N
    #for i in range(K):
    #    B[A[i]-1]=1
    #print(B)
    #for i in range(Q):
    #    if B[L[i]-1]==1:
    #        pass
    #    else:
    #        if B[L[i]]==0:
    #            B[L[i]]=1
    #        else:
    #            B[L[i]-2]=1
    #print(B)
    #for i in range(K):
    #    if B[i]==1:
    #        print(i+1,end=' ')
    #print()

    #空间复杂度O(N)
    #时间复杂度O(Q)
    #B=[0]*N
    #for i in range(K):
    #    B[A[i]-1]=1
    #print(B)
    #for i in range(Q):
    #    if B[L[i]-1]==1:
    #        pass
    #    else:
    #        if B[L[i]]==0:
    #            B[L[i]]=1
    #        else:
    #            B[L[i]-2]=1
    #print(B)
    #for i in range(K):
    #    if B[i]==1:
    #        print(i+1,end=' ')
    #print()

    #空间复杂度O(N)
    #时间复杂度O(Q)
    #B=[0]*N
    #for i in range(K):
    #    B[A[i]-1]=1
    #print(B)
    #for i in range(Q):
    #    if B[L[i]-1]==1:
    #        pass
    #    else:
    #        if B[L[i]]==0:
    #            B[L[i]]=1
    #        else:
    #            B[L[i]-2]=1
    #print(B)
    #for i in range(K):
    #    if B[i]==1:
    #        print(i

=======
Suggestion 5

def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    for i in range(q):
        if a[l[i]-1] < n:
            if a[l[i]-1]+1 in a:
                pass
            else:
                a[l[i]-1] += 1
    for i in range(k):
        print(a[i],end = ' ')

=======
Suggestion 6

def problem257_b():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))

    # 1. 棋子位置
    chess = [0] * N
    for i in range(K):
        chess[A[i] - 1] = 1

    # 2. 棋子移动
    for i in range(Q):
        current = L[i] - 1
        while current < N - 1:
            if chess[current + 1] == 1:
                break
            else:
                chess[current] = 0
                chess[current + 1] = 1
                current += 1

    # 3. 输出结果
    for i in range(K):
        for j in range(N):
            if chess[j] == 1:
                print(j + 1, end=' ')
    print()

=======
Suggestion 7

def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    for i in range(q):
        if a[l[i]-1] == n:
            pass
        else:
            if a[l[i]-1] == a[l[i]]:
                pass
            else:
                a[l[i]-1] += 1
    for i in range(k):
        print(a[i])

=======
Suggestion 8

def main():
    #读取输入
    #N K Q
    N,K,Q = map(int, input().split())
    #A_1 A_2 ...A_K
    A = list(map(int, input().split()))
    #L_1 L_2 ...L_Q
    L = list(map(int, input().split()))
    
    #棋子位置
    pos = [0]*N
    #初始化棋子位置
    for i in range(K):
        pos[A[i]-1] = 1

    #print(pos)
    #print(L)

    #执行操作
    for i in range(Q):
        #print(L[i])
        #print(pos)
        #print(pos[L[i]-1])
        #print(pos[L[i]])
        if pos[L[i]-1] == 1:
            continue
        elif pos[L[i]] == 0:
            pos[L[i]-1] = 0
            pos[L[i]] = 1
        else:
            continue
    #print(pos)
    #输出
    for i in range(N):
        if pos[i] == 1:
            print(i+1, end=" ")
    print()

=======
Suggestion 9

def main():
    N, K, Q = map(int, input().split())
    A = [int(x) for x in input().split()]
    L = [int(x) for x in input().split()]
    #print(N, K, Q)
    #print(A)
    #print(L)

    #棋子的位置
    chess = [0] * K
    for i in range(K):
        chess[i] = A[i]
    #print(chess)

    #操作
    for i in range(Q):
        #print("第%d次操作" % (i+1))
        #print("棋子位置：", chess)
        #print("操作：", L[i])
        #print("棋子位置：", chess)
        #print("操作：", L[i])
        #如果左边的第L_i个棋子在其最右边的方格上，则不做任何操作。
        if chess[L[i]-1] == N:
            continue
        #否则，如果右边的下一个方格上没有棋子，则将左边的第L_i个棋子向右移动一个方格；
        #如果有，则不做任何操作。
        else:
            if chess[L[i]-1] + 1 in chess:
                continue
            else:
                chess[L[i]-1] += 1

    #print("棋子位置：", chess)
    #print("操作：", L[i])
    #print("棋子位置：", chess)
    #print("操作：", L[i])
    #print("棋子位置：", chess)
    #print("操作：", L[i])

    #打印
    for i in range(K):
        print(chess[i], end=" ")
    print()

=======
Suggestion 10

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))

    # 棋子位置
    p = [0] * n
    for i in range(k):
        p[a[i] - 1] += 1
    # print(p)

    # 棋子移动
    for i in range(q):
        for j in range(k):
            if p[a[l[j] - 1] - 1] == 1:
                break
            if a[l[j] - 1] == n:
                continue
            p[a[l[j] - 1] - 1] -= 1
            p[a[l[j] - 1]] += 1
            a[l[j] - 1] += 1
        # print(p)
    # print(a)
    # print(l)

    # 输出
    for i in range(k):
        print(a[l[i] - 1], end=' ')
