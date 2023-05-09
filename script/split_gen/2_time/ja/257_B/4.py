def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    #print(N, K, Q)
    #print(A)
    #print(L)
    #print("")
    #init
    B = [0] * (N+1)
    for i in range(K):
        B[A[i]] = 1
    #print(B)
    for i in range(Q):
        #print(i, L[i])
        if B[L[i]] == 1:
            #print("B[L[i]] == 1")
            if L[i] == N:
                #print("L[i] == N")
                pass
            else:
                if B[L[i]+1] == 0:
                    #print("B[L[i]+1] == 0")
                    B[L[i]] = 0
                    B[L[i]+1] = 1
        else:
            #print("B[L[i]] == 0")
            pass
        #print(B)
    for i in range(1, N+1):
        if B[i] == 1:
            print(i, end=" ")
    print("")
