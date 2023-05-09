def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if min(A) > K:
        print(0)
        return
    if max(A) == K:
        print(N)
        return
    left = 0
    right = 0
    sum = 0
    cnt = 0
    while right < N:
        while right < N and sum < K:
            sum += A[right]
            right += 1
        while left <= right and sum >= K:
            sum -= A[left]
            left += 1
            cnt += N - right + 1
    print(cnt)

if __name__ == '__main__':
    main()