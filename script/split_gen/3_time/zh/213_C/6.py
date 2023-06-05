def main():
    H,W,N = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    print(A)
    print(B)
    #for i in range(N):
    #    for j in range(N):
    #        if A[i] == A[j] and B[i] == B[j]:
    #            print(i+1,j+1)
    #            break
    #        elif A[i] == A[j] and B[i] != B[j]:
    #            print(i+1,B[j])
    #            break
    #        elif A[i] != A[j] and B[i] == B[j]:
    #            print(A[j],j+1)
    #            break
    #        elif A[i] != A[j] and B[i] != B[j]:
    #            print(A[j],B[j])
    #            break
