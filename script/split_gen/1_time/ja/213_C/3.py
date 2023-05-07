def main():
    H,W,N = map(int,input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i],B[i] = map(int,input().split())
    A.sort()
    B.sort()
    C = [0]*N
    D = [0]*N
    for i in range(N):
        C[i] = A.index(A[i])+1
        D[i] = B.index(B[i])+1
    for i in range(N):
        print(C[i],D[i])
