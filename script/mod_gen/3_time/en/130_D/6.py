def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = 0
    right = 0
    total = 0
    for left in range(N):
        while right < N and total < K:
            total += A[right]
            right += 1
        if total < K:
            break
        result += N - right + 1
        total -= A[left]
    print(result)

if __name__ == '__main__':
    main()