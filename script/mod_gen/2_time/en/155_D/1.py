def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] >= 0:
        print(A[K-1])
        return
    if A[-1] <= 0:
        if K % 2 == 0:
            print(-A[-K])
        else:
            print(A[-K])
        return
    # A[0] < 0 < A[-1]
    if K % 2 == 0:
        if abs(A[0]) > abs(A[-1]):
            print(-A[-K])
        else:
            print(A[K-1])
        return
    # K % 2 == 1
    # A[0] < 0 < A[-1]
    # A[0] < 0 < A[-1] < 0
    if A[0] < 0 and A[-1] < 0:
        print(-A[-K])
        return
    # A[0] < 0 < 0 < A[-1]
    # A[0] < 0 < 0 < A[-1] < 0
    if A[0] < 0 and A[-1] > 0:
        if abs(A[0]) > abs(A[-1]):
            print(-A[-K])
        else:
            print(A[K-1])
        return
    # 0 < A[0] < A[-1]
    if A[0] > 0 and A[-1] > 0:
        print(A[K-1])
        return
    # 0 < A[0] < A[-1] < 0
    if A[0] > 0 and A[-1] < 0:
        print(A[K-1])
        return
    # 0 < A[0] < 0 < A[-1]
    if A[0] > 0 and A[-1] > 0:
        print(A[K-1])
        return
    # 0 < A[0] < 0 < A[-1] < 0
    if A[0] > 0 and A[-1] < 0:
        print(A[K-1])
        return
    # 0 < 0 < A[0] < A

if __name__ == '__main__':
    main()