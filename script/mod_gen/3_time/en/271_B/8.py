def main():
    # Read input data
    N, Q = map(int, input().split())
    L = [0] * N
    A = [0] * N
    for i in range(N):
        L[i] = int(input().split()[0])
        A[i] = list(map(int, input().split()))
    S = [0] * Q
    T = [0] * Q
    for i in range(Q):
        S[i], T[i] = map(int, input().split())
    # Calculate cumulative sum
    cumsum = [0] * (N + 1)
    for i in range(N):
        cumsum[i + 1] = cumsum[i] + L[i]
    # Find the answer
    for i in range(Q):
        print(A[S[i] - 1][T[i] - 1])

if __name__ == '__main__':
    main()