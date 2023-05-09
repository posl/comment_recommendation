def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    D = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(M):
        C[i], D[i] = map(int, input().split())
    ans = "No"
    for i in range(2 ** N):
        P = [0] * N
        for j in range(N):
            if ((i >> j) & 1):
                P[j] = 1
        flag = True
        for j in range(M):
            if (P[A[j] - 1] != P[B[j] - 1]):
                flag = False
        for j in range(M):
            if (P[C[j] - 1] != P[D[j] - 1]):
                flag = False
        if (flag):
            ans = "Yes"
            break
    print(ans)
main()

if __name__ == '__main__':
    main()