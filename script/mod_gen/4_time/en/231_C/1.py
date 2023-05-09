def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for i in range(Q):
        x = X[i]
        idx = bisect_left(A, x)
        print(N - idx)

if __name__ == '__main__':
    main()