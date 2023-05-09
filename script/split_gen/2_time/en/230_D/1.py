def main():
    N, D = map(int, input().split())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    L.sort()
    R.sort()
    ans = 0
    i = 0
    j = 0
    cnt = 0
    while i < N and j < N:
        if L[i] <= R[j]:
            cnt += 1
            i += 1
        else:
            cnt -= 1
            j += 1
        ans = max(ans, cnt)
    print(ans)
