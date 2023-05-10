def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N-1):
        if A[i] > A[i+1]:
            if i+K >= N:
                print("No")
                return
            A[i], A[i+K] = A[i+K], A[i]
            if A[i] > A[i+1]:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    solve()