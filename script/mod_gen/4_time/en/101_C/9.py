def problem101_c():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    min_num = 0
    for i in range(N):
        if i == 0:
            min_num = A[i]
        else:
            if min_num > A[i]:
                min_num = A[i]
    print((N-1) // (K-1))
problem101_c()

if __name__ == '__main__':
    problem101_c()