def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = N * (N + 1) // 2
    ans = 0
    for i in range(N):
        ans += (N - i) * (i + 1) * A[i]
    print(ans)
