def main():
    N, M = map(int, input().split())
    for i in range(N):
        for j in range(N):
            print(min(abs(i - k) + abs(j - l) for k in range(N) for l in range(N) if (k - i) * (k - i) + (l - j) * (l - j) == M), end=" ")
        print()
