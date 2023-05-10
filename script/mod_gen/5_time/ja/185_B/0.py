def main():
    N, M, T = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    now = N
    for i in range(M):
        if i == 0:
            now -= A[i]
        else:
            now -= A[i] - B[i-1]
        if now <= 0:
            print('No')
            exit()
        now += B[i] - A[i]
        if now > N:
            now = N
    now -= T - B[-1]
    if now <= 0:
        print('No')
        exit()
    print('Yes')

if __name__ == '__main__':
    main()