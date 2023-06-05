def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if N % K != 0:
        print("No")
        return
    for i in range(N - K):
        if A[i] > A[i + K]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    solve()