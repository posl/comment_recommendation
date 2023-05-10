Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))

    #print(N, K, Q)
    #print(A)
    #print(L)

    #N個のマスのリストを作成
    #マスにコマがあるかどうか��

=======
Suggestion 2

def move(masu, koma):
    if masu[koma-1] == 1:
        masu[koma-1] = 0
        masu[koma] = 1
    return masu

=======
Suggestion 3

def main():
    n,k,q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    b = [0] * n
    for i in range(k):
        b[a[i]-1] += 1
    for i in range(q):
        b = [x-1 for x in b]
        b[l[i]-1] += 1
    for i in range(n):
        if b[i] > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 4

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))

    #print(N, K, Q)
    #print(A)
    #print(L)

    #コマの位置を配列で持つ
    comas = [0] * N
    for i in range(K):
        comas[A[i]-1] += 1
    #print(comas)

    #コマの移動を行う
    for i in range(Q):
        #print("L[i]-1 = " + str(L[i]-1))
        #print("comas = " + str(comas))
        #print("comas[L[i]-1] = " + str(comas[L[i]-1]))
        if comas[L[i]-1] == 0:
            #print("comas[L[i]-1] == 0")
            continue
        else:
            comas[L[i]-1] -= 1
            comas[L[i]] += 1

    #print(comas)

    #コマの位置を出力
    for i in range(N):
        if comas[i] > 0:
            print(i+1, end=" ")
    print()

=======
Suggestion 5

def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    ans = [0] * n
    for i in range(k):
        ans[a[i]-1] += 1
    for i in range(q):
        ans[l[i]-1] += 1
    for i in range(n):
        if ans[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    koma = [0] * n
    for i in range(k):
        koma[a[i]-1] += 1
    for i in range(q):
        koma[l[i]-1] += 1
    for i in range(n):
        if koma[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

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

=======
Suggestion 8

def solve():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    ans = [0] * n

    for i in range(k):
        ans[a[i] - 1] += 1

    for i in range(q):
        ans[l[i] - 1] += 1

    for i in range(n):
        if ans[i] > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 9

def move_piece(board, piece):
    for i in range(len(board)):
        if board[i] == piece:
            if i == len(board) - 1:
                return board
            elif board[i + 1] == 0:
                board[i + 1] = board[i]
                board[i] = 0
                return board
            else:
                return board
    return board

=======
Suggestion 10

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    #print(n, k, q)
    #print(a)
    #print(l)

    #aのリストに対応するコマを追加
    ka = []
    for i in range(n):
        ka.append(0)
    for i in range(k):
        ka[a[i]-1] = 1
    #print(ka)

    #lのリストを逆順にして、操作を行う
    for i in range(q-1, -1, -1):
        #print(l[i])
        #print(ka)
        #print(ka[l[i]-1])
        #print(ka[l[i]])
        if ka[l[i]-1] == 1 and ka[l[i]] == 0:
            ka[l[i]] = 1
            ka[l[i]-1] = 0
        #print(ka)
        #print("")

    #kaのリストからコマのあるマスを出力
    for i in range(n):
        if ka[i] == 1:
            print(i+1, end=" ")
    print("")
