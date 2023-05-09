def main():
    N, M, Q = map(int, input().split())
    ABCD = [list(map(int, input().split())) for i in range(Q)]
    ans = 0
    for A in itertools.combinations_with_replacement(range(1, M + 1), N):
        score = 0
        for a, b, c, d in ABCD:
            if A[b - 1] - A[a - 1] == c:
                score += d
        ans = max(ans, score)
    print(ans)

if __name__ == '__main__':
    main()