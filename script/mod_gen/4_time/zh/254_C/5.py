def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if K == 1:
        for i in range(1, N):
            if A[i - 1] >= A[i]:
                print("No")
                return
        print("Yes")
        return
    for i in range(N - K):
        if A[i] >= A[i + K]:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    solve()