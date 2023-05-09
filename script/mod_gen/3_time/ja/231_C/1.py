def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for _ in range(Q)]
    A.sort()
    for i in range(Q):
        print(N - bisect.bisect_left(A, x[i]))

if __name__ == '__main__':
    main()