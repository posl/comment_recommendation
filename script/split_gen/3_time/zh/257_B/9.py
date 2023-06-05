def main():
    N,K,Q = map(int,input().split())
    A = list(map(int,input().split()))
    L = list(map(int,input().split()))
    B = [0]*N
    for i in range(K):
        B[A[i]-1] += 1
    for i in range(Q):
        for j in range(K):
            if B[A[L[j]-1]-1] == 1:
                break
            else:
                B[A[L[j]-1]-1] -= 1
                A[L[j]-1] += 1
                B[A[L[j]-1]-1] += 1
    for i in range(K):
        print(A[i],end=' ')
    print()
main()
