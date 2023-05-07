def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    mod = [0] * M
    mod[0] = 1
    ans = 0
    mod_sum = 0
    for i in range(N):
        mod_sum += A[i]
        mod_sum %= M
        ans += mod[mod_sum]
        mod[mod_sum] += 1
    print(ans)

if __name__ == '__main__':
    main()