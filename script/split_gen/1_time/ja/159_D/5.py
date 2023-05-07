def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    ans = [0 for i in range(N+1)]
    cnt = [0 for i in range(N+1)]
    for i in range(1, N+1):
        cnt[A[i]] += 1
    for i in range(1, N+1):
        ans[i] = cnt[A[i]] - 1
    #print(cnt)
    #print(ans)
    for i in range(1, N+1):
        print((N-1) - ans[i])
