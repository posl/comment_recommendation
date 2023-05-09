def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = [0] * (N + 1)
    for i in range(N):
        sumA[i + 1] = sumA[i] + A[i]
    ans = float('-inf')
    for i in range(N - M + 1):
        ans = max(ans, sumA[i + M] - sumA[i] + M * A[i])
    print(ans)
