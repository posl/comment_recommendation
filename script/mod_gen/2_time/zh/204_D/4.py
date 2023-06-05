def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
    else:
        A = list()
        B = list()
        for i in range(M):
            a, b = map(int, input().split())
            A.append(a)
            B.append(b)
        # print(A)
        # print(B)
        for i in range(M):
            A.append(B[i])
            B.append(A[i])
        # print(A)
        # print(B)
        C = [0 for i in range(N)]
        for i in range(M * 2):
            C[A[i] - 1] += 1
        # print(C)
        sum = 0
        for i in range(N):
            sum += C[i] * (C[i] - 1) / 2
        print(int(sum))

if __name__ == '__main__':
    main()