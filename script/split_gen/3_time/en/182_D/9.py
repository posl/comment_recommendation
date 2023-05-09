def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    
    #N = 3
    #A = [2, -1, -2]
    
    #N = 5
    #A = [-2, 1, 3, -1, -1]
    
    #N = 5
    #A = [-1000, -1000, -1000, -1000, -1000]
    
    B = [0] * N
    B[0] = A[0]
    for i in range(1, N):
        B[i] = B[i-1] + A[i]
    
    #print(B)
    
    C = [0] * N
    C[0] = B[0]
    for i in range(1, N):
        C[i] = max(C[i-1], B[i])
    
    #print(C)
    
    D = [0] * N
    D[0] = max(0, A[0])
    for i in range(1, N):
        D[i] = max(D[i-1], 0) + A[i]
    
    #print(D)
    
    E = [0] * N
    E[0] = D[0]
    for i in range(1, N):
        E[i] = max(E[i-1], D[i])
    
    #print(E)
    
    ans = 0
    for i in range(N):
        ans = max(ans, C[i], E[i])
    
    print(ans)
