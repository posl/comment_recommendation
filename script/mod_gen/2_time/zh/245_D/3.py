def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_min = min(A)
    A_max = max(A)
    B_min = min(B)
    B_max = max(B)
    if abs(A_max - B_max) > K or abs(A_min - B_min) > K:
        print("No")
        return
    for i in range(N - 1):
        if abs(A[i] - A[i + 1]) > K and abs(B[i] - B[i + 1]) > K:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    solve()