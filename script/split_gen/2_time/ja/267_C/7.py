def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-M+1):
        ans = max(ans, sum((i+1)*A[i+j] for j in range(M)))
    print(ans)
