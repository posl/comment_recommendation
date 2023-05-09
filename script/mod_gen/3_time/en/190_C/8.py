def solve():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for m in range(M):
        A[m], B[m] = map(int, input().split())
    K = int(input())
    C = [0] * K
    D = [0] * K
    for k in range(K):
        C[k], D[k] = map(int, input().split())
    ans = 0
    for i in range(2 ** K):
        dish = [0] * (N + 1)
        for k in range(K):
            if (i >> k) & 1:
                dish[C[k]] += 1
            else:
                dish[D[k]] += 1
        cnt = 0
        for m in range(M):
            if dish[A[m]] > 0 and dish[B[m]] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    solve()