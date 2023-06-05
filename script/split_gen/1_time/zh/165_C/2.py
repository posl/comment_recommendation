def main():
    N, M, Q = map(int, input().split())
    a = [0] * Q
    b = [0] * Q
    c = [0] * Q
    d = [0] * Q
    for i in range(Q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
    ans = 0
    A = [1] * N
    while True:
        score = 0
        for i in range(Q):
            if A[b[i] - 1] - A[a[i] - 1] == c[i]:
                score += d[i]
        ans = max(ans, score)
        idx = N - 1
        while idx >= 0 and A[idx] == M:
            idx -= 1
        if idx < 0:
            break
        A[idx] += 1
        for j in range(idx + 1, N):
            A[j] = A[idx]
    print(ans)
