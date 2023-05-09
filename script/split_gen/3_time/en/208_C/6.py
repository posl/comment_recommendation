def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    #print(N, K, a)
    a.sort()
    ans = [0] * N
    #print(a)
    for i in range(N):
        if K <= 0:
            break
        if i == N-1:
            ans[i] += K
            break
        diff = a[i+1] - a[i]
        if K >= diff * (i+1):
            ans[i] += diff
            K -= diff * (i+1)
        else:
            ans[i] += K // (i+1)
            break
    #print(ans)
    for i in range(N):
        ans[i] += K // N
    for i in range(K % N):
        ans[i] += 1
    for i in range(N):
        print(ans[i])
