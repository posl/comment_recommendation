def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    B = [0] * (N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]
    for x in X:
        l = 0
        r = N
        while r - l > 1:
            m = (l + r) // 2
            if B[m] >= x:
                r = m
            else:
                l = m
        print(N - l)

if __name__ == '__main__':
    main()