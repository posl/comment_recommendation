def main():
    N,K = map(int,input().split())
    A = map(int,input().split())
    B = map(int,input().split())
    A = list(A)
    B = list(B)
    A.sort(reverse=True)
    B.sort(reverse=True)
    i = 0
    for j in range(K):
        while i<N:
            if A[i] == A[i+1]:
                i += 1
            else:
                if A[i] == A[i+1] and B[j] == i+1:
                    print("Yes")
                    return
                elif A[i] != A[i+1] and B[j] == i+1:
                    print("Yes")
                    return
                else:
                    i += 1
    print("No")
