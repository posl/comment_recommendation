def main():
    N, M = map(int, input().split())
    L = [0]*M
    R = [0]*M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    L.sort()
    R.sort()
    ans = 0
    for i in range(1, M):
        ans += L[i] - R[i-1] - 1
    print(ans + N - R[M-1] + L[0] - 1)
