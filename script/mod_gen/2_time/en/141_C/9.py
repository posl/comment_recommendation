def main():
    # Read data
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    # Solve
    score = [K - Q] * N
    for i in range(Q):
        score[A[i] - 1] += 1
    # Output
    for i in range(N):
        if score[i] > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()