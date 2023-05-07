def main():
    #input
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    #compute
    for i in range(N-K):
        A.remove(max(A))
    for i in range(K):
        B[i] = A[B[i]-1]
    if max(B) == max(A):
        print("Yes")
    else:
        print("No")
    #output
