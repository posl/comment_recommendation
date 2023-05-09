def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N ** 0.5) + 1):
        for j in range(i, N // i + 1):
            ans += min(N // (i * j), j) - i + 1
    print(ans)
