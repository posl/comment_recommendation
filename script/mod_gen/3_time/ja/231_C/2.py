def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for _ in range(Q)]
    A.sort()
    for i in range(Q):
        l, r = 0, N
        while r - l > 1:
            m = (r + l) // 2
            if A[m] <= x[i]:
                l = m
            else:
                r = m
        print(N - l)

if __name__ == '__main__':
    main()