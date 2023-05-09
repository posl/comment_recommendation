def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    left = 0
    right = 0
    sum = 0
    while left < N:
        while right < N and sum < K:
            sum += A[right]
            right += 1
        if sum >= K:
            ans += N - right + 1
        sum -= A[left]
        left += 1
    print(ans)

if __name__ == '__main__':
    main()