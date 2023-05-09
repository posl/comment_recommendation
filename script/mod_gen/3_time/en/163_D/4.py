def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    MOD = 10**9+7
    ans = 0
    for i in range(K, N+2):
        ans += (N-i+1)*i+1
        ans %= MOD
    print(ans)
main()

if __name__ == '__main__':
    main()