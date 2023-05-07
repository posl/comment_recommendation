def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = [0]
    for i in range(N):
        sumA.append(sumA[-1] + A[i])
    ans = 0
    for i in range(N-M+1):
        ans = max(ans, sumA[i+M] - sumA[i] + M*(M-1))
    print(ans)
