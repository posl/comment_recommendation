def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        i = bisect.bisect_left(A, x)
        print(N - i)

if __name__ == '__main__':
    main()