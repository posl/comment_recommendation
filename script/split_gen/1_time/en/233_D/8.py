def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for l in range(N):
        r = l
        sum = 0
        while r < N:
            sum += A[r]
            if sum == K:
                ans += 1
            r += 1
    print(ans)
