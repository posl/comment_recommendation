def main():
    N, M, Q = map(int, input().split())
    A = [0] * (N + 1)
    A[0] = 1
    A[N] = M
    score = 0
    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        if A[b] - A[a] == c:
            score += d
    print(score)
