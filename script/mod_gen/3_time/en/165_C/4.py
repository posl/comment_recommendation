def main():
    N, M, Q = map(int, input().split())
    Qs = []
    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        Qs.append((a, b, c, d))
    ans = 0
    for A in itertools.product(range(1, M + 1), repeat=N):
        score = 0
        for a, b, c, d in Qs:
            if A[b - 1] - A[a - 1] == c:
                score += d
        ans = max(ans, score)
    print(ans)

if __name__ == '__main__':
    main()