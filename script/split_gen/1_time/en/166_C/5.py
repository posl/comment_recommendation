def main():
    N, M = [int(x) for x in input().split()]
    H = [int(x) for x in input().split()]
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        ok = True
        for j in range(M):
            if A[j] == i + 1 and H[B[j] - 1] >= H[i]:
                ok = False
                break
            elif B[j] == i + 1 and H[A[j] - 1] >= H[i]:
                ok = False
                break
        if ok:
            ans += 1
    print(ans)
