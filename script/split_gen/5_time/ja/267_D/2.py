def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - M + 1):
        B = A[i:i + M]
        sum = 0
        for j in range(M):
            sum += (j + 1) * B[j]
        if sum > ans:
            ans = sum
    print(ans)
