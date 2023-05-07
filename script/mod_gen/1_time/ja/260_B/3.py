def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    A = A[:X]
    B = B[:Y]
    C = C[:Z]
    for i in range(N):
        if A.count(A[i]) > 1:
            A.remove(A[i])
        if B.count(B[i]) > 1:
            B.remove(B[i])
        if C.count(C[i]) > 1:
            C.remove(C[i])
    A = set(A)
    B = set(B)
    C = set(C)
    for i in range(N):
        if A & B & C:
            print(i+1)
            A.remove(A[i])
            B.remove(B[i])
            C.remove(C[i])
        elif A & B:
            print(i+1)
            A.remove(A[i])
            B.remove(B[i])
        elif A & C:
            print(i+1)
            A.remove(A[i])
            C.remove(C[i])
        elif B & C:
            print(i+1)
            B.remove(B[i])
            C.remove(C[i])
        elif A:
            print(i+1)
            A.remove(A[i])
        elif B:
            print(i+1)
            B.remove(B[i])
        elif C:
            print(i+1)
            C.remove(C[i])
        else:
            break

if __name__ == '__main__':
    main()