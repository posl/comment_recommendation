def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for i in range(Q)]
    point = [K] * N
    for i in range(Q):
        point[A[i] - 1] += 1
    for i in range(N):
        if point[i] - Q <= 0:
            print("No")
        else:
            print("Yes")

if __name__ == '__main__':
    main()