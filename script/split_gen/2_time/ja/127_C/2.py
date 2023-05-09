def main():
    N, M = map(int, input().split())
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    for i in range(M):
        l, r = map(int, input().split())
        L[l] += 1
        R[r] += 1
    ans = 0
    cnt = 0
    for i in range(1, N + 1):
        cnt += L[i]
        cnt -= R[i]
        if cnt == M:
            ans += 1
    print(ans)
