def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    sumA = [0]*(N+1)
    for i in range(N):
        sumA[i+1] = sumA[i]+A[i]
    ans = 0
    right = 0
    for left in range(N):
        while right < N+1 and sumA[right]-sumA[left] < K:
            right += 1
        ans += N+1-right
    print(ans)

if __name__ == '__main__':
    solve()