def main():
    N = int(input())
    X = [tuple(map(int, input().split())) for _ in range(N)]
    X.sort()
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += ((X[i][0] - X[j][0]) ** 2 + (X[i][1] - X[j][1]) ** 2) ** 0.5
    print(ans * 2 / N / (N - 1))
main()
