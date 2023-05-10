def main():
    N, X, Y = map(int, input().split())
    ans = [0] * N
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            d = min(j - i, abs(X - i) + abs(Y - j) + 1)
            ans[d] += 1
    for k in range(1, N):
        print(ans[k])
