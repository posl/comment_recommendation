def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(N, M)
    print(H)
    print(A)
    print(B)
    cnt = 0
    for i in range(N):
        flag = True
        for j in range(M):
            if A[j] == i + 1:
                if H[i] <= H[B[j] - 1]:
                    flag = False
            if B[j] == i + 1:
                if H[i] <= H[A[j] - 1]:
                    flag = False
        if flag:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()