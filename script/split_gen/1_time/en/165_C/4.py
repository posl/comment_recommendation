def main():
    N, M, Q = map(int, input().split())
    A = [1] * N
    score = 0
    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        if A[b-1] - A[a-1] == c:
            score += d
    print(score)
