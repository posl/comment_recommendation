def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] >= K:
            ans += 1
        for j in range(i+1, N):
            A[j] += A[j-1]
            if A[j] >= K:
                ans += 1
    print(ans)
