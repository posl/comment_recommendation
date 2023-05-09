def main():
    X, Y, N = map(int, input().split())
    ans = N * X
    for i in range(0, N + 1):
        for j in range(0, N - i + 1):
            if i + j == N:
                ans = min(ans, i * Y + j * X)
    print(ans)
