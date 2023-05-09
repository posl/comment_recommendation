def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    points = [K - Q] * N
    for i in range(Q):
        points[A[i] - 1] += 1
    for i in range(N):
        if points[i] > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()