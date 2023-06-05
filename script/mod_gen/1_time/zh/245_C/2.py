def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_max = max(A)
    B_max = max(B)
    if abs(A_max - B_max) > K:
        print('No')
        return
    if A_max > B_max:
        A, B = B, A
    A.sort()
    B.sort(reverse=True)
    for i in range(N):
        if A[i] + B[i] > K:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    solve()