def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    right = 0
    sum = 0
    for left in range(N):
        while right < N and sum < K:
            sum += A[right]
            right += 1
        if sum >= K:
            ans += N - right + 1
        sum -= A[left]
    print(ans)
