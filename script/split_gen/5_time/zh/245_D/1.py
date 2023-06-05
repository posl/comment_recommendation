def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    C = list(map(int,input().split()))
    B = [0]*(M+1)
    for i in range(N+M,0,-1):
        B[M-(N+M-i)] = C[i]
        for j in range(0,N+M-i):
            C[j] -= A[j]*C[i]
    print(" ".join(map(str,B)))
