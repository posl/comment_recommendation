def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = [0] * (N + 1)
    for i in range(N):
        sum_A[i + 1] = sum_A[i] + A[i]
    mod = [0] * M
    for i in range(N + 1):
        mod[sum_A[i] % M] += 1
    ans = 0
    for i in range(M):
        ans += mod[i] * (mod[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()