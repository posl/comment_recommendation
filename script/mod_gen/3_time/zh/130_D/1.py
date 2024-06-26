def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    right = 0
    total = 0
    for left in range(N):
        while right < N and total + A[right] < K:
            total += A[right]
            right += 1
        ans += right - left
        if left == right:
            right += 1
        else:
            total -= A[left]
    print(ans)

if __name__ == '__main__':
    main()