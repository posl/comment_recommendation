def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(N, M, H, A, B)
    #print(H[0:3])
    #print(A[0:3])
    #print(B[0:3])
    #print(H[A[0]-1], H[B[0]-1])
    #print(H[A[1]-1], H[B[1]-1])
    #print(H[A[2]-1], H[B[2]-1])
    #print(H[A[3]-1], H[B[3]-1])
    #print(H[A[4]-1], H[B[4]-1])
    #print(H[A[5]-1], H[B[5]-1])
    #print(H[0], H[2])
    #print(H[3], H[1])
    #print(H[3], H[2])
    #print(H[3], H[5])
    #print(H[3], H[5])
    #print(H[3], H[5])
    #print(H[0] > H[2])
    #print(H[3] > H[1])
    #print(H[3] > H[2])
    #print(H[3] > H[5])
    #print(H[3] > H[5])
    #print(H[3] > H[5])
    #print(H[0] > H[2] or H[3] > H[1] or H[3] > H[2] or H[3] > H[5] or H[3] > H[5] or H[3] > H[5])
    #print(H[0] > H[2] or H[3] > H[2] or H[3] > H[5])
    #print(H[0] > H[2] or H[3] > H[2] or H[3] > H[5])
    #print(H[0] > H[2] or H[3] > H[2] or H[3] > H[5])
