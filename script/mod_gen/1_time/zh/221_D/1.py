def solve():
    # N = int(input())
    # A = []
    # B = []
    # for i in range(N):
    #     a, b = map(int, input().split())
    #     A.append(a)
    #     B.append(b)
    N = 200000
    A = [1000000000] * N
    B = [1000000000] * N
    d = {}
    for i in range(N):
        for j in range(A[i], A[i] + B[i]):
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
    ans = [0] * N
    for i in range(N):
        ans[i] = d[i + 1]
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    solve()