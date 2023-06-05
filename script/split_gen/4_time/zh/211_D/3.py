def main():
    N,M = map(int,input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i],B[i] = map(int,input().split())
    #print(N,M,A,B)
    #print(A[0],B[0])
    #print(N in A)
    #print(N in B)
    if N in A and N in B:
        print(2)
    else:
        print(1)
