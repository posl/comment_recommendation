def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    ans = [0] * (K + 1)
    for i in range(K, 0, -1):
        ans[i] = pow(K // i, N, mod)
        for j in range(2 * i, K + 1, i):
            ans[i] -= ans[j]
            ans[i] %= mod
    for i in range(1, K + 1):
        print(ans[i])

if __name__ == '__main__':
    main()