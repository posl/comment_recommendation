def main():
    N, M, Q = map(int, input().split())
    A = [0] * N
    A[0] = 1
    A[-1] = M
    for i in range(N - 2):
        A[i + 1] = M - N + 2 + i
    max_score = 0
    while True:
        score = 0
        for i in range(Q):
            a, b, c, d = map(int, input().split())
            if A[b - 1] - A[a - 1] == c:
                score += d
        max_score = max(max_score, score)
        if not next_permutation(A):
            break
    print(max_score)
