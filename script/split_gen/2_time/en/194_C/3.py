def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += (A[i] - A[i - 1]) ** 2
    ans *= (N - 1)
    for i in range(1, N - 1):
        ans += (A[i + 1] - A[i - 1]) * (A[i] - A[i - 1]) - (A[i] - A[i - 1]) * (A[i] - A[i - 1])
    print(ans)
