def main():
    # Read input
    N, M, Q = map(int, input().split())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]
    # Initialize
    A = [1] * N
    score = 0
    max_score = 0
    # Loop
    while True:
        # Update score
        for a, b, c, d in queries:
            if A[b-1] - A[a-1] == c:
                score += d
        max_score = max(max_score, score)
        score = 0
        # Increment
        A[0] += 1
        for i in range(N):
            if A[i] > M:
                if i == N-1:
                    return max_score
                A[i] = 1
                A[i+1] += 1

if __name__ == '__main__':
    main()