def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        print(N - bisect.bisect_right(A, x))

if __name__ == '__main__':
    main()