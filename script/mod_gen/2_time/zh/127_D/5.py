def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    A.sort()
    C.sort()
    j = 0
    for i in range(N):
        if j < M and A[i] < C[M-j-1] and B[M-j-1] > 0:
            A[i] = C[M-j-1]
            B[M-j-1] -= 1
        else:
            j += 1
    print(sum(A))

if __name__ == '__main__':
    main()