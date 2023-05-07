def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        ans = 0
        if x < A[0]:
            ans = sum(A) - N * x
        elif x > A[-1]:
            ans = N * x - sum(A)
        else:
            l, r = 0, N
            while r - l > 1:
                m = (l + r) // 2
                if A[m] <= x:
                    l = m
                else:
                    r = m
            ans = (N - l) * (x - A[l]) + sum(A[l + 1:]) - sum(A[:l + 1]) - (l + 1) * (A[l] - x)
        print(ans)

if __name__ == '__main__':
    main()