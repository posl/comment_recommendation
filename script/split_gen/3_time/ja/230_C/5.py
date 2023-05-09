def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    ans = [["." for _ in range(S - R + 1)] for _ in range(Q - P + 1)]
    for i in range(P, Q + 1):
        for j in range(R, S + 1):
            if (i + j) % 2 == 0:
                continue
            if 1 - A <= i - A <= min(N - A, B - 1):
                ans[i - P][j - R] = "#"
            if 1 - A <= i - A <= min(N - A, N - B):
                ans[i - P][j - R] = "#"
    for i in range(Q - P + 1):
        print("".join(ans[i]))
