def main():
    N, M, Q = map(int, input().split())
    ABCD = [list(map(int, input().split())) for _ in range(Q)]
    A = [1] * N
    max_score = 0
    while True:
        score = 0
        for a, b, c, d in ABCD:
            if A[b - 1] - A[a - 1] == c:
                score += d
        max_score = max(max_score, score)
        for i in range(N - 1, -1, -1):
            if A[i] < M:
                A[i] += 1
                break
            else:
                A[i] = 1
        else:
            break
    print(max_score)

if __name__ == '__main__':
    main()