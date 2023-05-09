def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        ok = True
        for j in range(M):
            if A[j] == i + 1:
                if H[i] <= H[B[j] - 1]:
                    ok = False
                    break
            elif B[j] == i + 1:
                if H[i] <= H[A[j] - 1]:
                    ok = False
                    break
        if ok:
            ans += 1
    print(ans)
