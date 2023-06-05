def main():
    print("start")
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    C=list(map(int,input().split()))
    B=[0]*(M+1)
    for i in range(N+1):
        for j in range(M+1):
            B[j]+=A[i]*C[i+j]
    print(B)
    print(" ".join(map(str,B)))
    print("end")
