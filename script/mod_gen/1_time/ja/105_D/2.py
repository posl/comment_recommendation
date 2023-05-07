def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A_sum = [0] * (N+1)
    for i in range(N):
        A_sum[i+1] = A_sum[i] + A[i]
    A_mod = [0] * (N+1)
    for i in range(N+1):
        A_mod[i] = A_sum[i] % M
    A_mod_cnt = [0] * M
    for i in range(N+1):
        A_mod_cnt[A_mod[i]] += 1
    ans = 0
    for i in range(M):
        ans += A_mod_cnt[i] * (A_mod_cnt[i]-1) // 2
    print(ans)

if __name__ == '__main__':
    main()