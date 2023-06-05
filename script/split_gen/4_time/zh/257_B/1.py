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
