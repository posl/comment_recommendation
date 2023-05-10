def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    total = 0
    right = 0
    for left in range(N):
        while right < N and total < K:
            total += A[right]
            right += 1
        if total < K:
            break
        ans += N - right + 1
        if left == right:
            right += 1
        else:
            total -= A[left]
    print(ans)
solve()

if __name__ == '__main__':
    solve()