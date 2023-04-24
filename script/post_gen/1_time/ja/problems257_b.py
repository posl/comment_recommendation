Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    B = [0] * N
    for i in range(K):
        B[A[i] - 1] = i + 1
    for i in range(Q):
        if B[L[i] - 1] != 0:
            if L[i] < N:
                if B[L[i]] == 0:
                    B[L[i] - 1] = 0
                    B[L[i]] = L[i]
                    continue
            if L[i] == N:
                continue
        else:
            continue
    for i in range(N):
        if B[i] != 0:
            B[i] = i + 1
    print(*B)
    return

=======
Suggestion 2

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    for i in range(Q):
        if L[i] == 1:
            if A[0] == N:
                pass
            elif A[1] != A[0] + 1:
                A[0] += 1
        elif L[i] == K:
            if A[K-1] == N:
                pass
            elif A[K-1] != A[K-2] + 1:
                A[K-1] += 1
        else:
            if A[L[i]-1] == N:
                pass
            elif A[L[i]] != A[L[i]-1] + 1:
                A[L[i]-1] += 1
    for i in A:
        print(i, end=' ')

=======
Suggestion 3

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    B = [0] * (N + 1)
    for a in A:
        B[a] = 1
    for l in L:
        if B[l] == 1 and l < N:
            B[l] = 0
            B[l + 1] = 1
    for i in range(1, N + 1):
        if B[i] == 1:
            print(i, end=' ')

=======
Suggestion 4

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    #print(N, K, Q)
    #print(A)
    #print(L)
    #print(A[L[0]-1])
    #print(A[L[1]-1])
    #print(A[L[2]-1])
    #print(A[L[3]-1])
    #print(A[L[4]-1])
    #print(A[L[5]-1])
    #print(A[L[6]-1])
    #print(A[L[7]-1])
    #print(A[L[8]-1])
    #print(A[L[9]-1])
    #print(A[L[10]-1])
    #print(A[L[11]-1])
    #print(A[L[12]-1])
    #print(A[L[13]-1])
    #print(A[L[14]-1])
    #print(A[L[15]-1])
    #print(A[L[16]-1])
    #print(A[L[17]-1])
    #print(A[L[18]-1])
    #print(A[L[19]-1])
    #print(A[L[20]-1])
    #print(A[L[21]-1])
    #print(A[L[22]-1])
    #print(A[L[23]-1])
    #print(A[L[24]-1])
    #print(A[L[25]-1])
    #print(A[L[26]-1])
    #print(A[L[27]-1])
    #print(A[L[28]-1])
    #print(A[L[29]-1])
    #print(A[L[30]-1])
    #print(A[L[31]-1])
    #print(A[L[32]-1])
    #print(A[L[33]-1])
    #print(A[L[34]-1])
    #print(A[L[35]-1])
    #print(A[L[36]-1])
    #print(A[L[37]-1])
    #print(A[L[38]-1])
    #print(A[L[39]-1])
    #print(A[L[40]-1])
    #print(A[L[41]-1])
    #print(A[L[42]-1])
    #print(A[L[43]-1])
    #print

=======
Suggestion 5

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    for i in range(q):
        if l[i] == k and a[l[i]-1] < n:
            a[l[i]-1], a[l[i]] = a[l[i]], a[l[i]-1]
        elif l[i] != k and a[l[i]-1] < n and a[l[i]] > a[l[i]-1]:
            a[l[i]-1], a[l[i]] = a[l[i]], a[l[i]-1]
    for i in a:
        print(i, end=' ')

=======
Suggestion 6

def main():
    N,K,Q = map(int,input().split())
    A = list(map(int,input().split()))
    L = list(map(int,input().split()))
    for i in range(Q):
        if L[i] == 1:
            if A[0] == N:
                continue
            elif A[0] + 1 == A[1]:
                continue
            else:
                A[0] += 1
                A[1] -= 1
        elif L[i] == K:
            if A[K-1] == N:
                continue
            elif A[K-2] + 1 == A[K-1]:
                continue
            else:
                A[K-1] += 1
                A[K-2] -= 1
        else:
            if A[L[i]-1] == N:
                continue
            elif A[L[i]-2] + 1 == A[L[i]-1] or A[L[i]] + 1 == A[L[i]-1]:
                continue
            else:
                A[L[i]-1] += 1
                A[L[i]-2] -= 1
    print(*A)

=======
Suggestion 7

def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    for i in range(q):
        if l[i] == 1:
            a[l[i]-1],a[l[i]] = a[l[i]],a[l[i]-1]
        elif l[i] == k:
            a[l[i]-2],a[l[i]-1] = a[l[i]-1],a[l[i]-2]
        else:
            if a[l[i]-2] > a[l[i]]:
                a[l[i]-2],a[l[i]-1] = a[l[i]-1],a[l[i]-2]
            elif a[l[i]] > a[l[i]-1]:
                a[l[i]-1],a[l[i]] = a[l[i]],a[l[i]-1]
    for i in range(k):
        print(a[i],end=' ')

=======
Suggestion 8

def main():
    #入力
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    #Aの値を変えないようにコピー
    A_copy = A.copy()
    #コマを動かす
    for i in range(Q):
        #動かすコマの番号
        L_i = L[i]
        #動かすコマの位置
        A_i = A[L_i-1]
        #最後のコマでなければ
        if A_i != N:
            #コマの右にコマがなければ
            if A_i+1 not in A:
                #コマを右に移動
                A[L_i-1] += 1
                #移動したコマの左のコマを右に移動
                if A_i-1 in A:
                    A[A.index(A_i-1)] += 1
    #出力
    for i in range(K):
        print(A[i], end=" ")

=======
Suggestion 9

def main():
    N, K, Q = map(int,input().split())
    A = list(map(int,input().split()))
    L = list(map(int,input().split()))

    #K個のコマの位置を記録するリスト
    #コマの位置は1～Nの範囲であるため、インデックスとコマの位置を対応させるために0を追加
    #例：コマの位置が2の場合、2番目の要素に1を代入
    pos = [0] * (N+1)
    for i in range(K):
        pos[A[i]] = 1

    #Q回の操作を行う
    for i in range(Q):
        #左からL_i番目のコマが一番右のマスにあるか
        if L[i] == K:
            continue
        #左からL_i番目のコマがあるマスの1つ右のマスにコマが無いか
        if pos[L[i]+1] == 0:
            #コマを1つ右のマスに移動させる
            pos[L[i]+1] = 1
            pos[L[i]] = 0
        else:
            continue

    #コマの位置を出力する
    for i in range(1,N+1):
        if pos[i] == 1:
            print(i,end=" ")
    print()
