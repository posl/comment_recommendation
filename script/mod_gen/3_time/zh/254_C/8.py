def solve():
    # 输入
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # K=1的特殊情况
    if K == 1:
        for i in range(1, N):
            if A[i] <= A[i - 1]:
                print("No")
                exit()
        print("Yes")
        exit()
    # K>1的情况
    B = []
    for i in range(K):
        B.append(A[i])
    B.sort()
    for i in range(K):
        A[i] = B[i]
    for i in range(K, N):
        if A[i] < A[i - K]:
            print("No")
            exit()
        if A[i] == A[i - K]:
            B = []
            for j in range(i - K + 1, i + 1):
                B.append(A[j])
            B.sort()
            for j in range(K):
                A[i - K + 1 + j] = B[j]
    print("Yes")

if __name__ == '__main__':
    solve()