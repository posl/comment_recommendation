def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    C = list(map(int,input().split()))
    B = []
    for i in range(M+1):
        B.append(0)
    for i in range(M+1):
        B[i] = C[i]
    for i in range(M+1):
        for j in range(N+1):
            B[i] -= A[j] * B[i-j]
    for i in range(M+1):
        print(B[i], end=" ")
