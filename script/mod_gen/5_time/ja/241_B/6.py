def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # N, M = 5, 2
    # A = [1,2,3,4,5]
    # B = [5,5]
    A.sort()
    B.sort()
    if M > N:
        print('No')
        exit()
    if min(A) < min(B):
        print('No')
        exit()
    if max(A) > max(B):
        print('No')
        exit()
    for i in range(M):
        if A[i] >= B[i]:
            print('No')
            exit()
    print('Yes')
    exit()

if __name__ == '__main__':
    main()