def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        total = 0
        for j in range(i, N):
            total += A[j]
            if total == K:
                ans += 1
    print(ans)
