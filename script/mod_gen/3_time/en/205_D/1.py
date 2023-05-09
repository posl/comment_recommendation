def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    A = [0] + A + [10**18]
    for k in K:
        l, r = 0, N + 1
        while r - l > 1:
            m = (l + r) // 2
            if A[m] - A[m - 1] - 1 < k:
                k -= A[m] - A[m - 1] - 1
                l = m
            else:
                r = m
        print(A[l] + k)

if __name__ == '__main__':
    main()