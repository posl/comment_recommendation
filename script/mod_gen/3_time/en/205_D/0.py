def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    A = [0] + A + [10**18]
    for k in K:
        l, r = -1, N
        while l + 1 < r:
            m = (l + r) // 2
            if A[m] < A[m + 1] - A[m] + 1:
                k -= A[m + 1] - A[m] + 1
                l = m
            else:
                r = m
        print(A[l] + k)

if __name__ == '__main__':
    main()