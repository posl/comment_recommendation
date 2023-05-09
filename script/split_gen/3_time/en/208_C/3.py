def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = [0] + a
    ans = [0] * (N + 1)
    for i in range(N):
        if a[i + 1] - a[i] > 1:
            ans[i + 1] = (a[i + 1] - a[i] - 1) * (i + 1)
    ans = [0] + list(map(int, np.cumsum(ans)))
    for i in range(N):
        if K >= ans[i + 1]:
            continue
        else:
            K -= ans[i]
            break
    if K == 0:
        print(a[i])
    else:
        print(a[i] + 1 + (K - 1) // (i + 1))
