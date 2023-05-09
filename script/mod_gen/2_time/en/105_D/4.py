def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_mod_M = [0] * (N + 1)
    for i in range(N):
        sum_mod_M[i + 1] = (sum_mod_M[i] + A[i]) % M
    ans = 0
    from collections import Counter
    cnt = Counter(sum_mod_M)
    for v in cnt.values():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()