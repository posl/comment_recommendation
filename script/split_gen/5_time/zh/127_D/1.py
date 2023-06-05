def main():
    N,M = input().split()
    N = int(N)
    M = int(M)
    A = input().split()
    A = list(map(int,A))
    B = []
    C = []
    for i in range(M):
        b,c = input().split()
        B.append(int(b))
        C.append(int(c))
    A.sort()
    C.sort(reverse=True)
    for i in range(M):
        if A[N-1] < C[i]:
            A[N-1] = C[i]
            B[i] -= 1
            if B[i] == 0:
                break
            else:
                C[i] = A[N-1]
                C.sort(reverse=True)
        else:
            break
    print(sum(A))
