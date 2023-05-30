def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    s = 0
    cnt = 0
    ans = 0
    for i in range(N):
        while s < K:
            if cnt == N:
                break
            s += A[cnt]
            cnt += 1
        if s < K:
            break
        ans += N-cnt+1
        s -= A[i]
    print(ans)
main()
