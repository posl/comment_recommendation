def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # A = [3, 0, 2, 5, 5, 3, 0, 6, 3]
    # M = 7
    # N = 9
    # A = [18, 16, 15, 9, 8, 8, 17, 1, 3, 17, 11, 9, 12, 11, 7, 3, 2, 14, 3, 12]
    # M = 20
    # N = 20
    A.sort()
    if N == 1:
        print((M - A[0]) % M)
        return
    # print(A)
    ans = 0
    for i in range(N - 1):
        ans += (A[i + 1] - A[i] - 1) % M
    ans += (A[0] + M - A[N - 1] - 1) % M
    print(ans)
