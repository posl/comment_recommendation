Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    for i in range(q):
        if a[l[i]-1] < a[l[i]]:
            a[l[i]-1] += 1
    for i in range(k):
        print(a[i],end=" ")
    print()

=======
Suggestion 2

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    # print(n, k, q)
    # print(a)
    # print(l)
    # print(a[0])
    # print(a[1])
    # print(a[2])
    # print(a[3])
    # print(a[4])
    # print(a[5])
    # print(a[6])
    # print(a[7])
    # print(a[8])
    # print(a[9])
    # print(a[10])
    # print(a[11])
    # print(a[12])
    # print(a[13])
    # print(a[14])
    # print(a[15])
    # print(a[16])
    # print(a[17])
    # print(a[18])
    # print(a[19])
    # print(a[20])
    # print(a[21])
    # print(a[22])
    # print(a[23])
    # print(a[24])
    # print(a[25])
    # print(a[26])
    # print(a[27])
    # print(a[28])
    # print(a[29])
    # print(a[30])
    # print(a[31])
    # print(a[32])
    # print(a[33])
    # print(a[34])
    # print(a[35])
    # print(a[36])
    # print(a[37])
    # print(a[38])
    # print(a[39])
    # print(a[40])
    # print(a[41])
    # print(a[42])
    # print(a[43])
    # print(a[44])
    # print(a[45])
    # print(a[46])
    # print(a[47])
    # print(a[48])
    # print(a[49])
    # print(a[50])
    # print(a[51])
    # print(a[52])
    # print(a[53])
    # print(a[54])
    # print(a[55])
    # print(a[56])
    # print(a[57])
    # print(a[58])
    # print(a[59])
    # print(a[60])
    # print(a[61])
    # print(a[62])
    #

=======
Suggestion 3

def get_input():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    return N, K, Q, A, L

=======
Suggestion 4

def main():
    # 读取输入
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    # 棋子位置
    P = []
    for i in range(K):
        P.append(A[i])
    # 棋子移动
    for i in range(Q):
        if P[L[i] - 1] != N:
            if P[L[i] - 1] + 1 not in P:
                P[L[i] - 1] += 1
    # 输出
    for i in range(K):
        print(P[i], end=' ')

=======
Suggestion 5

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    b = [0] * n
    for i in range(k):
        b[a[i] - 1] = 1
    for i in range(q):
        for j in range(l[i] - 1, n - 1):
            if b[j] == 1 and b[j + 1] == 0:
                b[j], b[j + 1] = b[j + 1], b[j]
    for i in range(n):
        if b[i] == 1:
            print(i + 1, end=" ")

=======
Suggestion 6

def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    for i in range(q):
        for j in range(k):
            if l[j] == n:
                continue
            if a[l[j]-1] == a[l[j]]:
                continue
            if a[l[j]] == a[l[j]-1]+1:
                a[l[j]-1],a[l[j]] = a[l[j]],a[l[j]-1]
    print(*a)

=======
Suggestion 7

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    ans = [0] * N

    for i in range(K):
        ans[A[i] - 1] += 1
    for i in range(Q):
        ans = ans[-1:] + ans[:-1]
        ans[L[i] - 1] += 1
    for i in range(N):
        if ans[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    # print(N, K, Q)
    # print(A)
    # print(L)
    # print(len(A), len(L))
    # print(A[0])
    # print(L[0])

    # 棋子初始位置
    chess = [0 for _ in range(N)]
    for i in range(K):
        chess[A[i]-1] += 1
    # print(chess)

    # 棋子移动
    for i in range(Q):
        for j in range(N):
            if chess[j] == 1 and j != N-1 and chess[j+1] == 0:
                chess[j] -= 1
                chess[j+1] += 1
                break
    # print(chess)

    # 棋子位置
    for i in range(K):
        print(chess[L[i]-1], end=" ")
    print()

=======
Suggestion 9

def main():
    n,k,q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    ans = [0 for i in range(n)]
    for i in range(k):
        ans[a[i]-1] += 1
    for i in range(n-1):
        ans[i+1] += ans[i]
    for i in range(q):
        print(ans[l[i]-1])
