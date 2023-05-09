def main():
    N, L = map(int, input().split())
    ans = 0
    if L >= 0:
        ans = L * N + (N * (N - 1)) // 2 - L
    elif L + N - 1 < 0:
        ans = L * N + (N * (N - 1)) // 2 - L - N + 1
    else:
        ans = L * N + (N * (N - 1)) // 2
    print(ans)
