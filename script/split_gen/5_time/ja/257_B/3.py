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
