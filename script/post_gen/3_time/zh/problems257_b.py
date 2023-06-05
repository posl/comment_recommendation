Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    #print(n,k,q)
    #print(a)
    #print(l)
    #pr

=======
Suggestion 2

def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    #print(a)
    #print(l)
    #print(k)

=======
Suggestion 3

def main():
    # 读入问题数据
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))

    # 生成棋子的位置列表
    chess = [0] * n
    for i in range(k):
        chess[a[i] - 1] = 1

    # 执行Q次操作
    for i in range(q):
        # 棋子移动
        if chess[l[i] - 1] == 1:
            for j in range(n):
                if chess[j] == 0:
                    chess[j] = 1
                    chess[l[i] - 1] = 0
                    break

    # 打印结果
    for i in range(n):
        if chess[i] == 1:
            print(i + 1, end=" ")
    print()

=======
Suggestion 4

def main():
    N, K, Q = map(int, input().split())
    A = [int(i) for i in input().split()]
    L = [int(i) for i in input().split()]
    B = [0] * N
    for i in range(K):
        B[A[i] - 1] += 1
    for i in range(N):
        if B[i] > 0:
            B[i] = 1
    for i in range(N - 1):
        B[i + 1] += B[i]
    for i in range(Q):
        print(B[L[i] - 1])

=======
Suggestion 5

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    # print(n, k, q)
    # print(a)
    # print(l)
    # print()

    # n, k, q = 5, 3, 5
    # a = [1, 3, 4]
    # l = [3, 3, 1, 1, 2]
    # print(n, k, q)
    # print(a)
    # print(l)
    # print()

    # n, k, q = 2, 2, 2
    # a = [1, 2]
    # l = [1, 2]
    # print(n, k, q)
    # print(a)
    # print(l)
    # print()

    # n, k, q = 10, 6, 9
    # a = [1, 3, 5, 7, 8, 9]
    # l = [1, 2, 3, 4, 5, 6, 5, 6, 2]
    # print(n, k, q)
    # print(a)
    # print(l)
    # print()

    # n, k, q = 200, 200, 1000
    # a = [i for i in range(1, 201)]
    # l = [i for i in range(1, 201)]
    # print(n, k, q)
    # print(a)
    # print(l)
    # print()

    # n, k, q = 200, 200, 1000
    # a = [i for i in range(1, 201)]
    # l = [i for i in range(1, 201)]
    # print(n, k, q)
    # print(a)
    # print(l)
    # print()

    # n, k, q = 200, 200, 1000
    # a = [i for i in range(1, 201)]
    # l = [i for i in range(1, 201)]
    # print(n, k, q)
    # print(a)
    # print(l

=======
Suggestion 6

def get_input():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    return N, K, Q, A, L

=======
Suggestion 7

def main():
    n,k,q = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    l = [int(x) for x in input().split()]
    #print(n,k,q,a,l)
    #print(a)
    #print(l)
    #print(len(a))
    #print(len(l))
    #print(a[0])
    #print(a[1])
    #print(a[2])
    #print(a[3])
    #print(a[4])
    #print(a[5])
    #print(a[6])
    #print(a[7])
    #print(a[8])
    #print(a[9])
    #print(a[10])
    #print(a[11])
    #print(a[12])
    #print(a[13])
    #print(a[14])
    #print(a[15])
    #print(a[16])
    #print(a[17])
    #print(a[18])
    #print(a[19])
    #print(a[20])
    #print(a[21])
    #print(a[22])
    #print(a[23])
    #print(a[24])
    #print(a[25])
    #print(a[26])
    #print(a[27])
    #print(a[28])
    #print(a[29])
    #print(a[30])
    #print(a[31])
    #print(a[32])
    #print(a[33])
    #print(a[34])
    #print(a[35])
    #print(a[36])
    #print(a[37])
    #print(a[38])
    #print(a[39])
    #print(a[40])
    #print(a[41])
    #print(a[42])
    #print(a[43])
    #print(a[44])
    #print(a[45])
    #print(a[46])
    #print(a[47])
    #print(a[48])
    #print(a[49])
    #print(a[50])
    #print(a[51])
    #print(a[52])
    #print(a[53])
    #print(a[54])
    #print(a[55])
    #print(a[56])
    #print(a[57])
    #print(a[58])
    #print(a[59])
    #print

=======
Suggestion 8

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    B = [0 for i in range(N)]
    for i in range(K):
        B[A[i] - 1] += 1
    for i in range(N):
        B[i] = 1 if B[i] > 0 else 0
    for i in range(Q):
        if B[L[i] - 1] == 0:
            continue
        elif L[i] == N:
            continue
        elif B[L[i]] == 0:
            B[L[i]] = 1
            B[L[i] - 1] = 0
        else:
            continue
    for i in range(N):
        if B[i] == 1:
            print(i + 1, end=' ')
    print()

=======
Suggestion 9

def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    flag = [0] * n
    for i in a:
        flag[i-1] += 1
    for i in l:
        if i == 1:
            if flag[0] == 0:
                flag[0] = 1
        else:
            if flag[i-1] == 0:
                flag[i-1] = 1
            else:
                flag[i-1] = 0
                flag[i] = 1
    for i in range(n):
        if flag[i] == 1:
            print(i+1,end=' ')
    print()

=======
Suggestion 10

def main():
    N,K,Q = map(int,input().split())
    A = list(map(int,input().split()))
    L = list(map(int,input().split()))
    B = [0]*N
    for i in range(K):
        B[A[i]-1] += 1
    for i in range(Q):
        for j in range(K):
            if B[A[L[j]-1]-1] == 1:
                break
            else:
                B[A[L[j]-1]-1] -= 1
                A[L[j]-1] += 1
                B[A[L[j]-1]-1] += 1
    for i in range(K):
        print(A[i],end=' ')
    print()

main()
