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
