def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    min_A = min(A)
    max_A = max(A)
    min_B = min(B)
    max_B = max(B)
    if (min_A > max_B) or (min_B > max_A):
        print('No')
        exit()
    if K == 0:
        print('Yes')
        exit()
    for i in range(N):
        if abs(A[i] - B[i]) > K:
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()