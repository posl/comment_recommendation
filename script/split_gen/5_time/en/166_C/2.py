def main():
    N, M = [int(x) for x in input().split()]
    H = [int(x) for x in input().split()]
    A = []
    B = []
    for i in range(M):
        a, b = [int(x) for x in input().split()]
        A.append(a)
        B.append(b)
    #print(N, M, H, A, B)
    #print(H[A[0]-1], H[B[0]-1])
    #print(H[A[1]-1], H[B[1]-1])
    #print(H[A[2]-1], H[B[2]-1])
    #print(H[A[3]-1], H[B[3]-1])
    #print(H[A[4]-1], H[B[4]-1])
    good = [True] * N
    for i in range(M):
        if H[A[i]-1] <= H[B[i]-1]:
            good[A[i]-1] = False
        if H[B[i]-1] <= H[A[i]-1]:
            good[B[i]-1] = False
    #print(good)
    print(good.count(True))
