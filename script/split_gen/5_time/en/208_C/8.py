def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0]*N
    for i in range(N):
        if K >= N:
            ans[i] = 1
        else:
            ans[i] = 0
        K = max(0, K-1)
    for i in range(N):
        print(ans[i])
main()
