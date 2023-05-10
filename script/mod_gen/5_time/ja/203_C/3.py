def main():
    N, K = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    for i in range(N):
        if K < A[i]:
            print(K)
            exit()
        K = K + B[i]
    print(K)

if __name__ == '__main__':
    main()