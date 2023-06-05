def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        if i == 0:
            B.append(A[i])
        else:
            B.append(B[i-1] + A[i])
    C = []
    for i in range(N):
        if i == 0:
            C.append(A[i])
        else:
            C.append(C[i-1] + B[i])
    D = []
    for i in range(N):
        if i == 0:
            D.append(A[i])
        else:
            D.append(D[i-1] + C[i])
    E = []
    for i in range(N):
        if i == 0:
            E.append(A[i])
        else:
            E.append(E[i-1] + D[i])
    min_value = 10**9
    for i in range(N-3):
        for j in range(i+1,N-2):
            for k in range(j+1,N-1):
                for l in range(k+1,N):
                    P = B[i]
                    Q = B[j] - B[i]
                    R = B[k] - B[j]
                    S = B[l] - B[k]
                    max_value = max(P,Q,R,S)
                    min_value = min(min_value, max_value - min(P,Q,R,S))
    print(min_value)

if __name__ == '__main__':
    main()