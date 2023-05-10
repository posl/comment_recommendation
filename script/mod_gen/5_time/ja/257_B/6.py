def main():
    N,K,Q = map(int,input().split())
    A = list(map(int,input().split()))
    L = list(map(int,input().split()))
    #print(N,K,Q)
    #print(A)
    #print(L)
    #print("")
    #マスのリストを作る
    m_list = []
    for i in range(1,N+1):
        m_list.append(i)
    #print(m_list)
    #print("")
    #コマのリストを作る
    c_list = []
    for i in range(K):
        c_list.append(A[i])
    #print(c_list)
    #print("")
    #操作を行う
    for i in range(Q):
        #コマが右端にあるか調べる
        if c_list[L[i]-1] == m_list[-1]:
            #右端にあるなら何もしない
            pass
        else:
            #右端にないなら、右隣にコマがあるか調べる
            if m_list.index(c_list[L[i]-1]) + 1 == m_list.index(c_list[L[i]-1] + 1):
                #右隣にコマがないなら、右隣にコマを移動させる
                m_list[m_list.index(c_list[L[i]-1])] = m_list[m_list.index(c_list[L[i]-1])] + 1
                #print(m_list)
            else:
                #右隣にコマがあるなら何もしない
                pass
    #print("")
    #コマの位置を出力する
    for i in range(K):
        print(m_list.index(c_list[i])+1,end=" ")

if __name__ == '__main__':
    main()