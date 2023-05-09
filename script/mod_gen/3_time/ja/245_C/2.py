def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N == 1:
        print('Yes')
        return
    if A[0] == B[0]:
        if N == 2:
            print('Yes')
            return
        else:
            for i in range(1, N):
                if abs(A[i] - A[i - 1]) > K:
                    print('No')
                    return
            print('Yes')
            return
    else:
        for i in range(1, N):
            if abs(A[i] - A[i - 1]) > K and abs(B[i] - B[i - 1]) > K and abs(A[i] - B[i]) > K:
                print('No')
                return
        print('Yes')
        return

if __name__ == '__main__':
    main()